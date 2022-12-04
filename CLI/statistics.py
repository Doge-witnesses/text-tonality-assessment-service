if __name__ == '__main__':
    
    from core import statistics_functions
    
else:
    
    from .core import statistics_functions

import pandas as pd


def frequency_ngrams(input_path: str, 
                    output_path: str,
                    sentiment: statistics_functions.commons.Sentiment, 
                    n: int = 1,
                    normalization: bool = True) -> None:
    """
        Counting the frequency of n-grams
        
        [input_path]    ---- path to processed dataset (.csv file)
        [output_path]   ---- save path
        [sentiment]     ---- make statistics by sentiment
        [n]             ---- size n-grams
        [normalization] ---- normalization of texts
    """
    
    dataset = statistics_functions.get_processed_texts(input_path)

    if sentiment == statistics_functions.commons.Sentiment.NEGATIVE:
        dataset = statistics_functions.get_neg_processed_texts(dataset)
    elif sentiment == statistics_functions.commons.Sentiment.POSITIVE:
        dataset = statistics_functions.get_pos_processed_texts(dataset)
    elif sentiment == statistics_functions.commons.Sentiment.NEUTRAL:
        dataset = statistics_functions.get_neu_processed_texts(dataset)
    
    stat = None
    
    if normalization:
        
        ngrams, dictionary = statistics_functions.get_norm_ngram(dataset, n)
        stat = statistics_functions.frequency_str(ngrams)
        
        for i in range(len(stat)):
            word, frequency = stat[i]
            stat[i] = (dictionary[word], frequency)
        
    else:
        
        ngrams = statistics_functions.get_ngram(dataset, n)
        stat = statistics_functions.frequency_str(ngrams)
    
    
    statistics_functions.save_frequency_str(stat, output_path)


if __name__ == '__main__':
    
    # frequency_ngrams('data/formatted_text_res.csv', 'data/res/formatted_text_pos_2gram_norm.csv', statistics_functions.commons.Sentiment.POSITIVE, 2, True)
    # frequency_ngrams('data/formatted_text_res.csv', 'data/res/formatted_text_pos_3gram_norm.csv', statistics_functions.commons.Sentiment.POSITIVE, 3, True)
    # frequency_ngrams('data/formatted_text_res.csv', 'data/res/formatted_text_neg_2gram_norm.csv', statistics_functions.commons.Sentiment.NEGATIVE, 2, True)
    # frequency_ngrams('data/formatted_text_res.csv', 'data/res/formatted_text_neg_3gram_norm.csv', statistics_functions.commons.Sentiment.NEGATIVE, 3, True)
    # frequency_ngrams('data/formatted_text_res.csv', 'data/res/formatted_text_neu_2gram_norm.csv', statistics_functions.commons.Sentiment.NEUTRAL, 2, True)
    # frequency_ngrams('data/formatted_text_res.csv', 'data/res/formatted_text_neu_3gram_norm.csv', statistics_functions.commons.Sentiment.NEUTRAL, 3, True)
    
    # frequency_ngrams('data/logical_parts_res.csv', 'data/res/logical_parts_pos_2gram_norm.csv', statistics_functions.commons.Sentiment.POSITIVE, 2, True)
    # frequency_ngrams('data/logical_parts_res.csv', 'data/res/logical_parts_pos_3gram_norm.csv', statistics_functions.commons.Sentiment.POSITIVE, 3, True)
    # frequency_ngrams('data/logical_parts_res.csv', 'data/res/logical_parts_neg_2gram_norm.csv', statistics_functions.commons.Sentiment.NEGATIVE, 2, True)
    # frequency_ngrams('data/logical_parts_res.csv', 'data/res/logical_parts_neg_3gram_norm.csv', statistics_functions.commons.Sentiment.NEGATIVE, 3, True)
    # frequency_ngrams('data/logical_parts_res.csv', 'data/res/logical_parts_neu_2gram_norm.csv', statistics_functions.commons.Sentiment.NEUTRAL, 2, True)
    # frequency_ngrams('data/logical_parts_res.csv', 'data/res/logical_parts_neu_3gram_norm.csv', statistics_functions.commons.Sentiment.NEUTRAL, 3, True)
    
    frequency_ngrams('data/formatted_text_res.csv', 'data/save.csv', statistics_functions.commons.Sentiment.POSITIVE, 3, True)
    
    