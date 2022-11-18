from transformers import AutoModelForTokenClassification, AutoTokenizer


def get_model():
    return AutoModelForTokenClassification.from_pretrained('cointegrated/rubert-tiny2-sentence-compression')
    
def get_tokenizer():
    return AutoTokenizer.from_pretrained('cointegrated/rubert-tiny2-sentence-compression')

def save_model(model, path):
    model.save_pretrained(path)
    
def save_tokenizer(tokenizer, path):
    tokenizer.save_pretrained(path)
    
    
def main():
    save_model(get_model(), 'core/object_review_models/compression/model_rubert_tiny2_sentence_compression/model_data/model')
    save_tokenizer(get_tokenizer(), 'core/object_review_models/compression/model_rubert_tiny2_sentence_compression/model_data/tokenizer')


main()
 