if __name__ == '__main__':

    from core import processing_functions
    
else:
    
    from .core import processing_functions

from enum import Enum
import pandas as pd

class _Preprocessing(Enum):
    
    WITHOUT_PREPROCESSING = 0
    TEXT_FORMATTING = 1
    LOGICAL_PARTS = 2


def text_tonality(preprocessing: _Preprocessing, input_text: str, object_review_size: int = 5):
    """Evaluation of tonality for input text"""
    
    if preprocessing == _Preprocessing.WITHOUT_PREPROCESSING:
        processed_text = processing_functions.processing_text(input_text, object_review_size)
        
        text = processed_text.text
        sentiment = processed_text.sentiment.name
        object_review = processed_text.object_review
        
        print('=' * 100, '\n')
        print(f'\tTEXT: \"{text}\"\n\tSENTIMENT: {sentiment}\n\tOBJECT: {object_review}\n')
        print('=' * 100)
        
    elif preprocessing == _Preprocessing.TEXT_FORMATTING:
        processed_text = processing_functions.processing_formatted_text(input_text, object_review_size)
        
        text = processed_text.text
        sentiment = processed_text.sentiment.name
        object_review = processed_text.object_review
        
        print('=' * 100, '\n')
        print(f'\tTEXT: \"{text}\"\n\tSENTIMENT: {sentiment}\n\tOBJECT: {object_review}\n')
        print('=' * 100)
        
    elif preprocessing == _Preprocessing.LOGICAL_PARTS:
        processed_logical_parts = processing_functions.processing_logical_parts(input_text, object_review_size).processed_texts

        for part_id in range(len(processed_logical_parts)):
            processed_text = processed_logical_parts[part_id]
        
            text = processed_text.text
            sentiment = processed_text.sentiment.name
            object_review = processed_text.object_review
            
            print('=' * 100, '\n')
            print(f'\tPART {part_id + 1}: \"{text}\"\n\tSENTIMENT: {sentiment}\n\tOBJECT: {object_review}\n')
            print('=' * 100)


if __name__ == '__main__':
    
    text = 'К сожалению,   заказ не отслеживается. Пропал... очень обидно... обратная связь с продавцом хорошая 	'
    
    text_tonality(input_text=text, 
                  preprocessing=_Preprocessing.WITHOUT_PREPROCESSING)
    
    text_tonality(input_text=text, 
                  preprocessing=_Preprocessing.TEXT_FORMATTING)
    
    text_tonality(input_text=text, 
                  preprocessing=_Preprocessing.LOGICAL_PARTS, object_review_size=3)
    
    # texts = pd.read_csv('data/phone.csv').dropna()['text'].to_list()
    
    # texts = texts[896+1792+21504:]
    
    # processing_functions.processing_with_buffer_reset(proc_fun=processing_functions.processing_logical_parts_dataset,
    #                                                   texts=texts,
    #                                                   output_path='data/res/phone_log_parts.csv',
    #                                                   object_review_size=4)
    
    # dataset1 = pd.read_csv('data/markup/women_data_with_markup1.csv',).drop('Unnamed: 0', axis=1)
    # dataset2 = pd.read_csv('data/markup/women_data_with_markup2.csv')
    # dataset3 = pd.read_csv('data/markup/women_data_with_markup3.csv').drop('Unnamed: 0', axis=1)
    # dataset4 = pd.read_csv('data/markup/women_data_with_markup4.csv', encoding='Windows 1251')
    # dataset5 = pd.read_csv('data/markup/women_data_with_markup1.csv').drop('Unnamed: 0', axis=1)
    
    # dataset = pd.concat([dataset1, dataset2, dataset3, dataset4, dataset5])
    
    # dataset.to_csv('data/markup/women_data_with_markup.csv', index=False)
    
    # texts = pd.read_csv('data/markup/women_data_with_markup.csv').dropna()['text'].to_list()
    
    # processing_functions.processing_with_buffer_reset(proc_fun=processing_functions.processing_formatted_dataset,
    #                                                   texts=texts,
    #                                                   output_path='data/markup/women_data_with_markup_res.csv',
    #                                                   object_review_size=4)
    