if __name__ == '__main__':
    
    from Bert_Russian_punctuation.bert_punctuation import Bert_punctuation
    
else:
    
    from .Bert_Russian_punctuation.bert_punctuation import Bert_punctuation
    

import re

class LogicalParts:
    def __init__(self):
        self.Bert_punctuation = Bert_punctuation()

    def transform(self, text):
        sents = [text]
        sents_punctuation = self.Bert_punctuation.predict(sents)
        result = re.split(', |\. |! |\\? |;', sents_punctuation[0])
        return result


logicalParts = LogicalParts()

def split_to_logical_parts(text):
    
    return logicalParts.transform(text)