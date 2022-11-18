import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer

model = AutoModelForTokenClassification.from_pretrained('core/object_review_models/compression/model_rubert_tiny2_sentence_compression/model_data/model')
tokenizer = AutoTokenizer.from_pretrained('core/object_review_models/compression/model_rubert_tiny2_sentence_compression/model_data/tokenizer')

def rubert_tiny2_compress(text, threshold=0.5, keep_ratio=None, all=False):
    """ Compress a sentence by removing the least important words.
    Parameters:
        threshold: cutoff for predicted probabilities of word removal
        keep_ratio: proportion of words to preserve
    By default, threshold of 0.5 is used.
    """
    with torch.inference_mode():
        tok = tokenizer(text, return_tensors='pt').to(model.device)
        proba = torch.softmax(model(**tok).logits, -1).cpu().numpy()[0, :, 1]
    if keep_ratio is not None:
        threshold = sorted(proba)[int(len(proba) * keep_ratio)]
    kept_toks = []
    keep = False
    prev_word_id = None
    
    if (all):
        mp = {}
        for word_id, score, token in zip(tok.word_ids(), proba, tok.input_ids[0]):
            mp[score] = token
        
        list_ = list()
        for i in sorted(mp):
            list_.append(mp[i])
        
        return tokenizer.decode(list_, skip_special_tokens=True)
                
    for word_id, score, token in zip(tok.word_ids(), proba, tok.input_ids[0]):
        if word_id is None:
            keep = True
        elif word_id != prev_word_id:
            keep = score < threshold
        if keep:
            kept_toks.append(token)
        prev_word_id = word_id
    return tokenizer.decode(kept_toks, skip_special_tokens=True)