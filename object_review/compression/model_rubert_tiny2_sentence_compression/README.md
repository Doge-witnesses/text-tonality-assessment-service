## Описание модели rubert_tiny2_sentence_compression 

Эту модель можно использовать для сжатия предложений (извлекающее обобщение предложений).

Он предсказывает для каждого слова, можно ли исключить это слово из предложения, не сильно повлияв на его значение.

Полученные предложения часто неграмматичны, но все же могут быть полезны.

Модель rubert-tiny2 настроена на наборе данных из статьи Сжатие предложений для русского языка: набор данных и базовые показатели .

### Пример использования:
import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer
model_name = 'cointegrated/rubert-tiny2-sentence-compression'
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


def compress(text, threshold=0.5, keep_ratio=None):
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
    for word_id, score, token in zip(tok.word_ids(), proba, tok.input_ids[0]):
        if word_id is None:
            keep = True
        elif word_id != prev_word_id:
            keep = score < threshold
        if keep:
            kept_toks.append(token)
        prev_word_id = word_id
    return tokenizer.decode(kept_toks, skip_special_tokens=True)


text = 'Кроме того, можно взять идею, рожденную из сердца, и выразить ее в рамках одной '\
    'из этих структур, без потери искренности идеи и смысла песни.'
    
print(compress(text))
print(compress(text, threshold=0.3))
print(compress(text, threshold=0.1))
# можно взять идею, рожденную из сердца, и выразить ее в рамках одной из этих структур.
# можно взять идею, рожденную из сердца выразить ее в рамках одной из этих структур.
# можно взять идею рожденную выразить структур.

print(compress(text, keep_ratio=0.5))
# можно взять идею, рожденную из сердца выразить ее в рамках структур.
