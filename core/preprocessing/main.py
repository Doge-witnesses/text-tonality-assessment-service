from Bert_Russian_punctuation.bert_punctuation import Bert_punctuation
import re

class LogicalParts:
    def __init__(self):
        self.Bert_punctuation = Bert_punctuation()

    def transform(self, text):
        sents = [text]
        sents_punctuation = self.Bert_punctuation.predict(sents)
        result = re.split(', |\. |! |\\? |;', sents_punctuation[0])
        return result

if __name__ == '__main__':
    parts = LogicalParts()
    sentences = parts.transform('В целом отель понравился номер был просторный но убирали редко было грязно в остальном все хорошо завтрак понравился')
    print(*sentences, sep='\n')