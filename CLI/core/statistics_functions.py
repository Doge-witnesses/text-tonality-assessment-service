if __name__ == '__main__':
    
    import commons
    from preprocessing.morphological_analysis import text_normalization
    from preprocessing.text_clear import text_clear

else:
    
    from . import commons
    from .preprocessing.morphological_analysis import text_normalization
    from .preprocessing.text_clear import text_clear

import pandas as pd


def get_processed_texts(path: str) -> commons._Dataset_processed_texts:
    """
        Getting a processed dataset from .csv file
        
        [path] ---- path to the dataset
    """
    
    df = pd.read_csv(path, lineterminator='\n').values.tolist()
    
    row_processed_texts = []
    
    for processed_texts in df:
        
        text = processed_texts[0]
        sentiment = None
        
        if processed_texts[1] == 'NEGATIVE':
            sentiment = commons.Sentiment.NEGATIVE
        elif processed_texts[1] == 'NEUTRAL':
            sentiment = commons.Sentiment.NEUTRAL
        elif processed_texts[1] == 'POSITIVE':
            sentiment = commons.Sentiment.POSITIVE
        
        object_review = text_clear(processed_texts[2]).split()
        
        if (text == None or sentiment == None or object_review == None):
            continue
        
        row_processed_texts.append(commons._Processed_text(text, sentiment, object_review))
        
    return commons._Dataset_processed_texts(row_processed_texts)


def get_pos_processed_texts(dataset: commons._Dataset_processed_texts) -> commons._Dataset_processed_texts:
    """
        Extracting POSITIVE texts from a dataset
    """

    res = []
    
    for processed_text in dataset.processed_texts:
        if processed_text.sentiment == commons.Sentiment.POSITIVE:
            res.append(processed_text)
            
    return commons._Dataset_processed_texts(res)


def get_neg_processed_texts(dataset: commons._Dataset_processed_texts) -> commons._Dataset_processed_texts:
    """
        Extracting NEGATIVE texts from a dataset
    """

    res = []
    
    for processed_text in dataset.processed_texts:
        if processed_text.sentiment == commons.Sentiment.NEGATIVE:
            res.append(processed_text)
            
    return commons._Dataset_processed_texts(res)


def get_neu_processed_texts(dataset: commons._Dataset_processed_texts) -> commons._Dataset_processed_texts:
    """
        Extracting NEUTRAL texts from a dataset
    """

    res = []
    
    for processed_text in dataset.processed_texts:
        if processed_text.sentiment == commons.Sentiment.NEUTRAL:
            res.append(processed_text)
            
    return commons._Dataset_processed_texts(res)


def frequency_str(ngrams: list[str]) -> list[tuple[str, int]]:
    """
        Computing frequency of words in a list
        
        [words] ---- list of words
    """
    
    frequency = {}
    
    for ngram in ngrams:
        
        if frequency.get(ngram, None):
            frequency[ngram] += 1
        else:
            frequency[ngram] = 1
                
    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        
    return frequency


def get_ngram(dataset_processed_texts: commons._Dataset_processed_texts, n: int = 1) -> list[str]:
    """
       Getting n_grams from a processed dataset of texts 
    """
    
    res = []
    
    for processed_text in dataset_processed_texts.processed_texts:
        for i in range(len(processed_text.object_review) - n + 1):
            res.append(' '.join(processed_text.object_review[i:i + n]))
            
    return res


def get_norm_ngram(dataset_processed_texts: commons._Dataset_processed_texts, n: int = 1) -> tuple[list[str], dict[str, str]]:
    """
       Getting and normalizing n_grams from a processed dataset of texts
    """
    
    res = []
    dictionary = {}
    
    for processed_text in dataset_processed_texts.processed_texts:
        for i in range(len(processed_text.object_review) - n + 1):
            string = ' '.join(processed_text.object_review[i:i + n])
            res.append(' '.join(sorted(text_normalization(string).split())))
            dictionary[res[-1]] = string
            
    return res, dictionary

def save_frequency_str(frequency_str : list[tuple[str, int]], save_path: str) -> None:
    """
        Save the frequency of words in .csv format
    """
    
    df = pd.DataFrame(frequency_str, columns=['Words', 'Frequency'])
    
    df.to_csv(save_path)