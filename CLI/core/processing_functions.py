if __name__ == '__main__':
    
    from object_review_models.compression.compressor import compress
    from sentiment_analysis_models.predictor import predict
    from preprocessing import preprocessing
    from preprocessing.text_clear import text_clear
    import commons

else:
    
    from .object_review_models.compression.compressor import compress
    from .sentiment_analysis_models.predictor import predict
    from .preprocessing import preprocessing
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
    
    if len(text) < 100:
        logical_parts = preprocessing.preprocessing2(text)
    else:
        logical_parts = preprocessing.preprocessing1(text)
        
    processed_parts = []
    
    for part in logical_parts:
        
        processed_parts.append(processing_text(part, object_review_size))
        
    return commons._Dataset_processed_texts(processed_parts)


def processing_dataset(texts : list[str], object_review_size: int = 3) -> commons._Dataset_processed_texts:
    """
        Computing of sentiment and object review in dataset
        
        [texts]              ---- Dataset of texts 
        [object_review_size] ---- Number of words in object review
    """
    
    res = []
    
    for text in texts:
        
        res.append(processing_text(text, object_review_size))
        
        
    return commons._Dataset_processed_texts(res)


def processing_formatted_dataset(texts : list[str], object_review_size: int = 3) -> commons._Dataset_processed_texts:
    """
        Text formatting and computing of sentiment and object review in dataset
        
        [texts]              ---- Dataset of texts 
        [object_review_size] ---- Number of words in object review
    """
    
    res = []
    
    for text in texts:
        
        res.append(processing_formatted_text(text, object_review_size))
        
        
    return commons._Dataset_processed_texts(res)


def processing_logical_parts_dataset(texts : list[str], object_review_size: int = 3) -> commons._Dataset_processed_texts:
    """
        Dividing text into logical parts and computing of sentiment and object review in dataset
        
        [texts]              ---- Dataset of texts 
        [object_review_size] ---- Number of words in object review
    """
    
    res = []
    
    for text in texts:
        for processed_part in processing_logical_parts(text, object_review_size).processed_texts:
            
            res.append(processed_part)
        
        
    return commons._Dataset_processed_texts(res)
    

def save_dataset(dataset: commons._Dataset_processed_texts, output_path: str) -> None:
    """
        Saving a dataset of processed texts
        
        [dataset]     ---- Processed texts
        [output_path] ---- Save path
    """
    
    df = pd.DataFrame(dataset.unwrappe(), columns=['Text', 'Sentiment', 'Object_review'])
    
    df.to_csv(output_path)
    
def processing_with_buffer_reset(proc_fun, texts : list[str], output_path: str, object_review_size: int = 3, buffer_size: int = 128) -> commons._Dataset_processed_texts:
    """
        Processing and saving texts in packages
        
        [proc_fun]           ---- Processing function
        [texts]              ---- Dataset of texts 
        [output_path]        ---- Save path
        [object_review_size] ---- Number of words in object review
        [buffer_size]        ---- Package size
    """
    
    pd.DataFrame(columns=['Text', 'Sentiment', 'Object_review']).to_csv(output_path, index=False)
    
    for i in range((len(texts) + buffer_size - 1)//buffer_size):
        
        df = pd.DataFrame(proc_fun(texts[i*buffer_size:min((i+1)*buffer_size, len(texts))], object_review_size).unwrappe(), columns=['Text', 'Sentiment', 'Object_review'])
        
        df.to_csv(output_path, mode='a', index=False, header=False)
        
        print('Text: ', min((i + 1) * buffer_size, len(texts)))