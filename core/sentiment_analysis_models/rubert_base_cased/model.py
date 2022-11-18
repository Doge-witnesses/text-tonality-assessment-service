import torch
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast

model = AutoModelForSequenceClassification.from_pretrained('core/sentiment_analysis_models/rubert_base_cased/model_data/model')
tokenizer = BertTokenizerFast.from_pretrained('core/sentiment_analysis_models/rubert_base_cased/model_data/tokenizer')

def rubert_base_cased(text):
    # (str) -> int
    inputs = tokenizer(text, max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
    predicted = torch.argmax(predicted, dim=1).numpy()
    return predicted[0]

