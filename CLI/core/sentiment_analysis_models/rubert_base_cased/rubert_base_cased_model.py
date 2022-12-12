import torch
from transformers import BertForSequenceClassification, BertTokenizer

rubert_base_cased_model = BertForSequenceClassification.from_pretrained('core/sentiment_analysis_models/rubert_base_cased/model_data/model')
rubert_base_cased_tokenizer = BertTokenizer.from_pretrained('core/sentiment_analysis_models/rubert_base_cased/model_data/tokenizer')

def rubert_base_cased_predict(text):
    # (str) -> int
    inputs = rubert_base_cased_tokenizer(text,max_length = 65,padding = 'max_length',truncation = True,return_tensors='pt')
    with torch.no_grad():
        model_output = rubert_base_cased_model(**inputs)
    output = model_output.logits
    output = torch.nn.functional.softmax(output, 1)
    return int(output.argmax(axis=1))
