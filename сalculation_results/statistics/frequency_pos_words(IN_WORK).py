if __name__ == '__main__':
    
    from core.object_review_models.compression.compressor import compress
    from core.sentiment_analysis_models.predictor import predict
    from core.preprocessing.preprocessing import preprocessing
    from core.preprocessing.formatting.punctuation import drop_space_and_punctuation

else:
    pass
    # from .core.object_review_models.compression.compressor import compress
    # from .core.sentiment_analysis_models.predictor import predict
    # from .core.preprocessing.preprocessing import preprocessing
    # from .core.preprocessing.formatting.punctuation import drop_space_and_punctuation

import pandas as pd


def frequency_positive_words(dataset):
    
    neg_dictionary = {}
    pos_dictionary = {}
    
    neg_texts = dataset[dataset['Sentiment'] == 'NEGATIVE']['Object'].to_list()
    pos_texts = dataset[dataset['Sentiment'] == 'POSITIVE']['Object'].to_list()
    
    for text in neg_texts:
        for object_rev in text:
            
            if neg_dictionary.get(object_rev, None):
                
                neg_dictionary[object_rev] += 1
                
            else:
            
                neg_dictionary[object_rev] = 1
                
    
    for text in pos_texts:
        for object_rev in text:
            
            if pos_dictionary.get(object_rev, None):
                
                pos_dictionary[object_rev] += 1
                
            else:
            
                pos_dictionary[object_rev] = 1         
    
            
    neg_dictionary = sorted(neg_dictionary.items(), key=lambda x: x[1], reverse=True)
    
    pos_dictionary = sorted(pos_dictionary.items(), key=lambda x: x[1], reverse=True)
        
    return pos_dictionary, neg_dictionary



def frequency_pos_words(input_path, size = 0):
    """Statistics on the frequency of review objects in positive texts
        
        (input_path, output_path, size = 0) -> void
        
        input_path  - .csv file [id, text, lable]
        output_path - .csv file [word, num words]
        size        - number of texts from the input file"""
    
    whole_text, formatted_text, logical_parts = dataset_input(input_path, size)
   
    dataset_output(whole_text, 'core/row_res/whole_text_res.csv')
    dataset_output(formatted_text, 'core/row_res/formatted_text_res.csv')
    dataset_output(logical_parts, 'core/row_res/logical_parts_res.csv')
    
    whole_text_statistics_pos, whole_text_statistics_neg = word_statistics(whole_text)
    formatted_text_statistics_pos, formatted_text_statistics_neg = word_statistics(formatted_text)
    logical_parts_statistics_pos, logical_parts_statistics_neg = word_statistics(logical_parts)
    
    dataset_output_word_statistics(whole_text_statistics_pos, 'core/row_res/statistics/whole_text_statistics_pos.csv')
    dataset_output_word_statistics(whole_text_statistics_neg, 'core/row_res/statistics/whole_text_statistics_neg.csv')
    
    dataset_output_word_statistics(formatted_text_statistics_pos, 'core/row_res/statistics/formatted_text_statistics_pos.csv')
    dataset_output_word_statistics(formatted_text_statistics_neg, 'core/row_res/statistics/formatted_text_statistics_neg.csv')
    
    dataset_output_word_statistics(logical_parts_statistics_pos, 'core/row_res/statistics/logical_parts_statistics_pos.csv')
    dataset_output_word_statistics(logical_parts_statistics_neg, 'core/row_res/statistics/logical_parts_statistics_neg.csv')
    
    
if __name__ == '__main__':
    
    dataset_statistics(input_path = 'data/women.csv', size = 10)