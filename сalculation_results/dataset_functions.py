if __name__ == '__main__':
    
    from ..core.object_review_models.compression.compressor import compress
    from ..core.sentiment_analysis_models.predictor import predict
    from ..core.preprocessing.preprocessing import preprocessing
    from ..core.preprocessing.formatting.punctuation import drop_space_and_punctuation

import pandas as pd


def processing_input_text(text, num_words = 3):
    """(str, int)   ->  list[[str](WHOLE_TEXT), [str](SENTIMENT), [list[str]](OBJECTS)]
                        list[[str](FORMATTED_TEXT), [str](SENTIMENT), [list[str]](OBJECTS)]
                        list[list[[str](LOGICAL_PART_TEXT), [str](SENTIMENT), [list[str]](OBJECTS)]]
    
    ===============================================
    
        The tonality of the text from the input 
        
    ===============================================
        
        text        -   Input text;
        num_words   -   Number of words for the output object review;"""  
    
    preproc_text = drop_space_and_punctuation(text) # temp
    logical_parts = preprocessing(text)
    
    text_sentiment = predict(text)
    text_object = compress(text, num_words)
    
    pre_text_sentiment = predict(preproc_text)
    pre_text_object = compress(preproc_text, num_words)
    
    res_whole_text = []
    res_formatted_text = []
    res_logical_part_text = []

    res_whole_text = [text, text_sentiment, text_object.split()]
    res_formatted_text = [preproc_text, pre_text_sentiment, pre_text_object.split()]
    
    for i in range(len(logical_parts)):
        
        if (len(logical_parts[i]) == 0):
            continue
        
        res_logical_part_text.append([logical_parts[i], predict(logical_parts[i]), compress(logical_parts[i], num_words).split()])
        
    
    return res_whole_text, res_formatted_text, res_logical_part_text



def processing_dataset_input(input_path, size, num_words = 3):
    """(str, int)   ->  DataFrame['Whole text', 'Sentiment', 'Objects']
                        DataFrame['Formatted text', 'Sentiment', 'Objects']
                        DataFrame['Logical part text', 'Sentiment', 'Objects']
                     
                     
    =======================================================
        
        The tonality of the text from the input dataset
        
    =======================================================
        
        
        input_path  -   Path to dataset (.csv file [id, text, lable]);
        size        -   Number of texts from the dataset;
        num_words   -   Number of words for the output object review;"""
    
    df = pd.read_csv(input_path, lineterminator='\n')
    
    texts = ''
    
    if (size > 0):
        
        texts = df['text'].head(size).to_list()
        
    else:
        
        texts = df['text'].to_list()
        
             
    whole_texts = []
    formatted_texts = []
    logical_parts_texts = []
    
    for i in range(len(texts)):
        
        whole_text_res, formatted_text, logical_parts_text = processing_input_text(texts[i], num_words)
        
        whole_texts.append(whole_text_res)
        formatted_texts.append(formatted_text)
        
        for j in logical_parts_text[2]:
        
            logical_parts_texts.append(j)
        
        print(f'Text: {i + 1}') ####################################### Time test !
        
    return  pd.DataFrame(whole_texts, columns=['Whole text', 'Sentiment', 'Objects']),\
            pd.DataFrame(formatted_texts, columns=['Formatted text', 'Sentiment', 'Objects']),\
            pd.DataFrame(logical_parts_texts, columns=['Logical part text', 'Sentiment', 'Objects'])


def save_dataset(df, output_path):
    """(DataFrame, str) ->  void
    
    ====================================
    
        Saving a dataset to .csv file
    
    ===================================="""
    
    
    df.to_csv(output_path)