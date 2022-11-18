from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast


def get_model():
    return AutoModelForSequenceClassification.from_pretrained('blanchefort/rubert-base-cased-sentiment', return_dict=True)
    
def get_tokenizer():
    return BertTokenizerFast.from_pretrained('blanchefort/rubert-base-cased-sentiment')

def save_model(model, path):
    model.save_pretrained(path)
    
def save_tokenizer(tokenizer, path):
    tokenizer.save_pretrained(path)
    
    
def main():
    save_model(get_model(), 'core/sentiment_analysis_models/model_test/model_data/model')
    save_tokenizer(get_tokenizer(), 'core/sentiment_analysis_models/model_test/model_data/tokenizer')


main()
 