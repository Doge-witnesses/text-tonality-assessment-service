if __name__ == '__main__':
    
    from object_review_models.compression.compressor import compress
    from sentiment_analysis_models.predictor import predict
    from preprocessing.preprocessing import preprocessing
    from preprocessing.formatting.punctuation import drop_space_and_punctuation
    from processing_functions import _Processed_text
    from processing_functions import Sentiment
    from processing_functions import _Dataset_processed_texts

else:
    
    from .object_review_models.compression.compressor import compress
    from .sentiment_analysis_models.predictor import predict
    from .preprocessing.preprocessing import preprocessing
    from .preprocessing.formatting.punctuation import drop_space_and_punctuation
    from .processing_functions import _Processed_text
    from .processing_functions import Sentiment
    from .processing_functions import _Dataset_processed_texts

import pandas as pd
    

def get_pos_processed_texts(dataset: _Dataset_processed_texts) -> _Dataset_processed_texts:
    """
        Extracting POSITIVE texts from a dataset
    """

    res = list[_Processed_text]
    
    for processed_text in dataset.dataset_processed_texts:
        if processed_text.sentiment == Sentiment.POSITIVE:
            res.append(processed_text)
            
    return res


def get_neg_processed_texts(dataset: _Dataset_processed_texts) -> _Dataset_processed_texts:
    """
        Extracting NEGATIVE texts from a dataset
    """

    res = list[_Processed_text]
    
    for processed_text in dataset.dataset_processed_texts:
        if processed_text.sentiment == Sentiment.NEGATIVE:
            res.append(processed_text)
            
    return res


def get_neu_processed_texts(dataset: _Dataset_processed_texts) -> _Dataset_processed_texts:
    """
        Extracting NEUTRAL texts from a dataset
    """

    res = list[_Processed_text]
    
    for processed_text in dataset.dataset_processed_texts:
        if processed_text.sentiment == Sentiment.NEUTRAL:
            res.append(processed_text)
            
    return res


def frequency_words(words: list[str]) -> list[tuple[str, int]]:
    """
        Computing frequency of words in a list
        
        [words] ---- list of words
    """
    
    frequency = dict[str, int]
    
    for word in words:
        
        if frequency.get(word, None):
            frequency[word] += 1
        else:
            frequency[word] = 1
                
    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        
    return frequency
