if __name__ == '__main__':
    
    from object_review_models.compression.compressor import compress
    from sentiment_analysis_models.predictor import predict
    from preprocessing.preprocessing import preprocessing
    from preprocessing.formatting.punctuation import drop_space_and_punctuation

else:
    
    from .object_review_models.compression.compressor import compress
    from .sentiment_analysis_models.predictor import predict
    from .preprocessing.preprocessing import preprocessing
    from .preprocessing.formatting.punctuation import drop_space_and_punctuation
    
import pandas as pd
from enum import Enum


class Sentiment(Enum):
    
    NEUTRAL = 0
    POSITIVE = 1
    NEGATIVE = 2


class _Processed_text(object):
    """
        Wrapper over the processed text
    """
    
    def __init__(self, text: str, sentiment: Sentiment, object_review: list[str]):
        
        self.text = text
        self.sentiment = sentiment
        self.object_review = object_review
        
    def unwrappe(self) -> list[str, str, list[str]]:
        
        return [self.text, self.sentiment.name, self.object_review]
            
            
class _Dataset_processed_texts(object):
    """
        Wrapper over the processed texts
    """
    
    def __init__(self, processed_texts: list[_Processed_text]):
        
        self.dataset_processed_texts = processed_texts
        
    def unwrappe(self) -> list[_Processed_text]:
        
        return self.dataset_processed_texts
    
    def unwrappe_to_list(self) -> list[list[str, str, list[str]]]:
        
        res = []
        
        for processed_text in self.unwrappe():
            res.append(processed_text.unwrappe())
        
        return res
    
    def objects_review_to_list(self):
        
        res = []
        
        for processed_text in self.dataset_processed_texts:
            for word in processed_text.object_review:
                res.append(word)
            
        return res

    
def processing_text(text: str, object_review_size: int = 3) -> _Processed_text:
    """
        Computing of sentiment and object review
        
        [text] ------------------ Input text        
        [object_review_size] ---- Number of words in object review
    """
    
    text_sentiment = predict(text)
    text_object = compress(text, object_review_size).split()
    
    return _Processed_text(text, Sentiment(text_sentiment), text_object)


def processing_formatted_text(text: str, object_review_size: int = 3) -> _Processed_text:
    """
        Text formatting and computing of sentiment and object review
        
        [text] ------------------ Input text        
        [object_review_size] ---- Number of words in object review
    """
    
    formatted_text = drop_space_and_punctuation(text) ######################################################## TEMP
    
    return processing_text(formatted_text, object_review_size)


def processing_logical_parts(text: str, object_review_size: int = 3) -> _Dataset_processed_texts:
    """
        Dividing text into logical parts and computing of sentiment and object review
        
        [text] ------------------ Input text        
        [object_review_size] ---- Number of words in object review
    """
    
    logical_parts = preprocessing(text)
    processed_parts = []
    
    for part in logical_parts:
        
        processed_parts.append(processing_text(part, object_review_size))
        
    return _Dataset_processed_texts(processed_parts)


def processing_dataset(input_path: str, size: int = 0, object_review_size: int = 3) -> _Dataset_processed_texts:
    """
        Computing of sentiment and object review in dataset
        
        [input_path] ------------ Path to dataset (.csv file [..., text, ...])
        [size] ------------------ Number of texts from the dataset 
        [object_review_size] ---- Number of words in object review
    """
    
    df = pd.read_csv(input_path, lineterminator='\n')
    texts = ''
    
    if (size > 0):
        texts = df['text'].head(size).to_list()
    else:
        texts = df['text'].to_list()
        
    res = list[_Processed_text]
    
    for text in texts:
        
        res.append(processing_text(text))
        
    return _Dataset_processed_texts(res)


def processing_formatted_dataset(input_path: str, size: int = 0, object_review_size: int = 3) -> _Dataset_processed_texts:
    """
        Text formatting and computing of sentiment and object review in dataset
        
        [input_path] ------------ Path to dataset (.csv file [..., text, ...])
        [size] ------------------ Number of texts from the dataset 
        [object_review_size] ---- Number of words in object review
    """
    
    df = pd.read_csv(input_path, lineterminator='\n')
    texts = ''
    
    if (size > 0):
        texts = df['text'].head(size).to_list()
    else:
        texts = df['text'].to_list()
        
    res = list[_Processed_text]
    
    for text in texts:
        
        res.append(processing_formatted_text(text))
        
    return _Dataset_processed_texts(res)


def processing_logical_parts_dataset(input_path: str, size: int = 0, object_review_size: int = 3) -> _Dataset_processed_texts:
    """
        Dividing text into logical parts and computing of sentiment and object review in dataset
        
        [input_path] ------------ Path to dataset (.csv file [..., text, ...])
        [size] ------------------ Number of texts from the dataset 
        [object_review_size] ---- Number of words in object review
    """
    
    df = pd.read_csv(input_path, lineterminator='\n')
    texts = ''
    
    if (size > 0):
        texts = df['text'].head(size).to_list()
    else:
        texts = df['text'].to_list()
        
    res = list[_Processed_text]
    
    for text in texts:
        for processed_part in processing_logical_parts(text):
            
            res.append(processed_part)
        
    return _Dataset_processed_texts(res)
    