if __name__ == '__main__':
    
    from core.object_review_models.compression.compressor import compress
    from core.sentiment_analysis_models.predictor import predict
    from core.preprocessing.preprocessing import preprocessing
    from core.preprocessing.formatting.punctuation import drop_space_and_punctuation

else:
    
    from .object_review_models.compression.compressor import compress
    from .sentiment_analysis_models.predictor import predict
    from .preprocessing.preprocessing import preprocessing
    from .preprocessing.formatting.punctuation import drop_space_and_punctuation

import pandas as pd

def cli_output(data):
    print('#' * 100, '\n')
    
    print('=' * 100)
    print(f'\tTEXT: \"{data[0][0]}\"\n\tSENTIMENT: {data[0][1]}\n\tOBJECT: {data[0][2]}')
    print('=' * 100)
    
    print('=' * 100)
    print(f'\tFORMATED TEXT: \"{data[1][0]}\"\n\tSENTIMENT: {data[1][1]}\n\tOBJECT: {data[1][2]}')
    print('=' * 100)
    
    for i in range(2, len(data)):
        print('=' * 100)
        print(f'\tLOGICAL PART {i - 1}: \"{data[i][0]}\"\n\tSENTIMENT: {data[i][1]}\n\tOBJECT: {data[i][2]}')
        print('=' * 100)
        
    print('\n', '#' * 100)


def cli_input(text, num_words = 3):
    """ The tonality of the text from the input stream 
        text        -   Input feedback
        num_words   -   The number of words for the output object review 
        
        -> list[list[text, sentiment, list[object]]]"""  
    
    preproc_text = drop_space_and_punctuation(text) # temp
    logical_parts = preprocessing(text)
    
    text_sentiment = predict(text)
    text_object = compress(text, num_words)
    
    pre_text_sentiment = predict(preproc_text)
    pre_text_object = compress(preproc_text, num_words)
    
    res = [[], [], []]

    res[0] = [text, text_sentiment, text_object.split()]
    res[1] = [preproc_text, pre_text_sentiment, pre_text_object.split()]
    
    for i in range(len(logical_parts)):
        
        if (len(logical_parts[i]) == 0):
            continue
        
        # logical_parts[i] = drop_space_and_punctuation(logical_parts[i])
        
        res[2].append([logical_parts[i], predict(logical_parts[i]), compress(logical_parts[i], num_words).split()])
        
    
    return res
    
    # temp (а может и не temp) :)
    
    
def dataset_output(df, output_path = 'core/res_df.csv'):
    
    df.to_csv(output_path)


def dataset_input(input_path, size):
    """(path) -> list[list[list[text, sentiment, list[object]]]]"""
    
    df = pd.read_csv(input_path, lineterminator='\n')
    
    texts = ''
    
    if (size > 0):
        
        texts = df['text'].head(size).to_list()
        
    else:
        
        texts = df['text'].to_list()
        
             
    whole_text_res = []
    formatted_text = []
    logical_parts = []
    
    for i in range(len(texts)):
        
        temp = cli_input(texts[i])
        
        whole_text_res.append(temp[0])
        formatted_text.append(temp[1])
        
        for j in temp[2]:
        
            logical_parts.append(j)
        
        print(f'Text: {i + 1}') # Time test !
        
    return  pd.DataFrame(whole_text_res, columns=['Whole text', 'Sentiment', 'Object']),\
            pd.DataFrame(formatted_text, columns=['Formatted text', 'Sentiment', 'Object']),\
            pd.DataFrame(logical_parts, columns=['Some part', 'Sentiment', 'Object'])


def word_statistics(dataset):
    
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


def dataset_output_word_statistics(dictionary, output_path = 'core/dataset_word_statistics.csv'):

    
    res_df = pd.DataFrame(dictionary, columns=['Word', 'Num words'])
    
    res_df.to_csv(output_path)


def cli_output_word_statistics(dictionary):
    
    print('#' * 100, '\n')
    
    for i in dictionary:
        
        print(f'{i[0]:-<20}: {i[1]}')


def dataset_statistics(input_path = 'data/women.csv', size = 5):
    
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
    """TEST: TODO - перенести по файлам"""
    
    # text = 'на фото все выглядело гораздо лучше чем оказалось в реальности. размер который я заказала оказался не просто большим а огромным!'
    
    # res = cli_input(text)
    
    # cli_output(res)
    
    dataset_statistics(size=0)
    