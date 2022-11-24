import torch
from transformers import BertForSequenceClassification,BertTokenizer
map_location=torch.device('cpu')

tokenizer = BertTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")
model = BertForSequenceClassification.from_pretrained("DeepPavlov/rubert-base-cased", 
                                                      num_labels = 3, 
                                                      output_attentions = False,
                                                      output_hidden_states = False)
model.load_state_dict(torch.load(PATH,map_location=map_location)) #PATH - путь к файлу model_1.pth
model.eval()

def rubert_base_cased(text):
    # (str) -> int
    inputs = tokenizer(text,max_length = 65,padding = 'max_length',truncation = True,return_tensors='pt')
    with torch.no_grad():
      model_output = model(**inputs)
    output = model_output.logits
    output = torch.nn.functional.softmax(output)
    return int(output.argmax(axis=1))

