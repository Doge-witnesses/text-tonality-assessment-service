from Bert_Russian_punctuation.bert_punctuation import Bert_punctuation
import sparknlp

from pyspark.ml import PipelineModel
from sparknlp.annotator import *
from sparknlp.base import *

class LogicalParts:
    def __init__(self):
        self.spark = sparknlp.start()
        self.Bert_punctuation = Bert_punctuation()

        self.documenter = DocumentAssembler()\
        .setInputCol("text")\
        .setOutputCol("document")

        self.sentencerDL = SentenceDetectorDLModel\
        .pretrained("sentence_detector_dl", "ru") \
        .setInputCols(["document"]) \
        .setOutputCol("sentences")

        self.sd_model = LightPipeline(PipelineModel(stages=[self.documenter, self.sentencerDL]))

    def transform(self, text):
        sents = [text]
        sents_punctuation = self.Bert_punctuation.predict(sents)
        sents_punctuation = sents_punctuation[0].replace(',', '.')
        result = self.sd_model.fullAnnotate(sents_punctuation)
        return(list(map(lambda x: x.result, result[0]['sentences'])))

if __name__ == '__main__':
    parts = LogicalParts()
    sentences = parts.transform('В целом отель понравился номер был просторный но убирали редко было грязно в остальном все хорошо завтрак понравился')
    print(*sentences, sep='\n')