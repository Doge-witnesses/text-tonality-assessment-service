import torch
from transformers import BertForSequenceClassification, BertTokenizer


def get_rubert_base_cased_model():
    model = BertForSequenceClassification.from_pretrained("DeepPavlov/rubert-base-cased", 
                                                      num_labels = 3, 
                                                      output_attentions = False,
                                                      output_hidden_states = False)
    
    model.load_state_dict(torch.load('core/sentiment_analysis_models/rubert_base_cased/model_data/model.pth', map_location=torch.device('cpu')))
    model.eval()
    return model
    
def get_rubert_base_cased_tokenizer():
    return BertTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")

def save_model(model, path):
    model.save_pretrained(path)
    
def save_tokenizer(tokenizer, path):
    tokenizer.save_pretrained(path)
    
    
def get_rubert_base_cased():
    
    save_model(get_rubert_base_cased_model(), 'core/sentiment_analysis_models/rubert_base_cased/model_data/model')
    save_tokenizer(get_rubert_base_cased_tokenizer(), 'core/sentiment_analysis_models/rubert_base_cased/model_data/tokenizer')

 