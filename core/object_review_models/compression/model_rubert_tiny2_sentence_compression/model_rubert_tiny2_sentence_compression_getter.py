from transformers import AutoModelForTokenClassification, AutoTokenizer


def get_rubert_tiny2_sentence_compression_model():
    return AutoModelForTokenClassification.from_pretrained('cointegrated/rubert-tiny2-sentence-compression')
    
def get_rubert_tiny2_sentence_compression_tokenizer():
    return AutoTokenizer.from_pretrained('cointegrated/rubert-tiny2-sentence-compression')

def save_model(model, path):
    model.save_pretrained(path)
    
def save_tokenizer(tokenizer, path):
    tokenizer.save_pretrained(path)
    
    
def get_rubert_tiny2_sentence_compression():
    save_model(get_rubert_tiny2_sentence_compression_model(), 'core/object_review_models/compression/model_rubert_tiny2_sentence_compression/model_data/model')
    save_tokenizer(get_rubert_tiny2_sentence_compression_tokenizer(), 'core/object_review_models/compression/model_rubert_tiny2_sentence_compression/model_data/tokenizer')

 