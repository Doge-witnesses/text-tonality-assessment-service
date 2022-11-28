from transformers import AutoModelForTokenClassification, AutoTokenizer


def _get_rubert_tiny2_sentence_compression_model():
    return AutoModelForTokenClassification.from_pretrained('cointegrated/rubert-tiny2-sentence-compression')
    
def _get_rubert_tiny2_sentence_compression_tokenizer():
    return AutoTokenizer.from_pretrained('cointegrated/rubert-tiny2-sentence-compression')

def _save_model(model, path):
    model.save_pretrained(path)
    
def _save_tokenizer(tokenizer, path):
    tokenizer.save_pretrained(path)
    
    
def get_rubert_tiny2_sentence_compression() -> None:
    
    _save_model(_get_rubert_tiny2_sentence_compression_model(), 'CLI/core/object_review_models/compression/model_rubert_tiny2_sentence_compression/model_data/model')
    _save_tokenizer(_get_rubert_tiny2_sentence_compression_tokenizer(), 'CLI/core/object_review_models/compression/model_rubert_tiny2_sentence_compression/model_data/tokenizer')

 