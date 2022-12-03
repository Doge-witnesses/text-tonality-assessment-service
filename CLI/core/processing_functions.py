if __name__ == '__main__':
    
    from object_review_models.compression.compressor import compress
    from sentiment_analysis_models.predictor import predict
    from preprocessing.preprocessing import preprocessing
    from preprocessing.text_clear import text_clear
    import commons

else:
    
    from .object_review_models.compression.compressor import compress
    from .sentiment_analysis_models.predictor import predict
    from .preprocessing.preprocessing import preprocessing
    from .preprocessing.text_clear import text_clear
    from . import commons
    
import pandas as pd


def processing_text(text: str, object_review_size: int = 3) -> commons._Processed_text:
    """
        Computing of sentiment and object review
        
        [text] ------------------ Input text        
        [object_review_size] ---- Number of words in object review
    """
    
    text_sentiment = predict(text)
    text_object = compress(text, object_review_size).split()
    
    return commons._Processed_text(text, commons.Sentiment(text_sentiment), text_object)


def processing_formatted_text(text: str, object_review_size: int = 3) -> commons._Processed_text:
    """
        Text formatting and computing of sentiment and object review
        
        [text] ------------------ Input text        
        [object_review_size] ---- Number of words in object review
    """
    
    formatted_text = text_clear(text)
    
    return processing_text(formatted_text, object_review_size)


def processing_logical_parts(text: str, object_review_size: int = 3) -> commons._Dataset_processed_texts:
    """
        Dividing text into logical parts and computing of sentiment and object review
        
        [text] ------------------ Input text        
        [object_review_size] ---- Number of words in object review
    """
    
    logical_parts = preprocessing(text)
    processed_parts = []
    
    for part in logical_parts:
        
        processed_parts.append(processing_text(part, object_review_size))
        
    return commons._Dataset_processed_texts(processed_parts)


def processing_dataset(input_path: str, size: int = 0, object_review_size: int = 3) -> commons._Dataset_processed_texts:
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
        
    res = list[commons._Processed_text]
    
    for text in texts:
        
        res.append(processing_text(text))
        
    return commons._Dataset_processed_texts(res)


def processing_formatted_dataset(input_path: str, size: int = 0, object_review_size: int = 3) -> commons._Dataset_processed_texts:
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
        
    res = list[commons._Processed_text]
    
    for text in texts:
        
        res.append(processing_formatted_text(text))
        
    return commons._Dataset_processed_texts(res)


def processing_logical_parts_dataset(input_path: str, size: int = 0, object_review_size: int = 3) -> commons._Dataset_processed_texts:
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
        
    res = list[commons._Processed_text]
    
    for text in texts:
        for processed_part in processing_logical_parts(text):
            
            res.append(processed_part)
        
    return commons._Dataset_processed_texts(res)
    