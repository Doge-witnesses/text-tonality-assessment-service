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
            
            
class _Dataset_processed_texts(object):
    """
        Wrapper over the processed texts
    """
    
    def __init__(self, processed_texts: list[_Processed_text]):
        
        self.processed_texts = processed_texts
