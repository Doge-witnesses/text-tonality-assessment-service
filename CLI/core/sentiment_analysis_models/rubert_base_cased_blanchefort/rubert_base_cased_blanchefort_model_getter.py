from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast


def get_rubert_base_cased_model():
    return AutoModelForSequenceClassification.from_pretrained('blanchefort/rubert-base-cased-sentiment', return_dict=True)
    
def get_rubert_base_cased_tokenizer():
    return BertTokenizerFast.from_pretrained('blanchefort/rubert-base-cased-sentiment')

def save_model(model, path):
    model.save_pretrained(path)
    
def save_tokenizer(tokenizer, path):
    tokenizer.save_pretrained(path)
    
    
def get_rubert_base_cased_blanchefort():
    
    save_model(get_rubert_base_cased_model(), 'CLI/core/sentiment_analysis_models/rubert_base_cased_blanchefort/model_data/model')
    save_tokenizer(get_rubert_base_cased_tokenizer(), 'CLI/core/sentiment_analysis_models/rubert_base_cased_blanchefort/model_data/tokenizer')

 