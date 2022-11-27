import torch
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast

tokenizer = BertTokenizerFast.from_pretrained('core/sentiment_analysis_models/rubert_base_cased_blanchefort/model_data/tokenizer')
model = AutoModelForSequenceClassification.from_pretrained('core/sentiment_analysis_models/rubert_base_cased_blanchefort/model_data/model', return_dict=True)


def rubert_base_cased_blanchefort_predict(text):
    #(str) -> str
    
    inputs = tokenizer(text, max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
    predicted = int(torch.argmax(predicted, dim=1).numpy())
    return predicted
