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
    
    # text = 'Товар так и не пришёл ((( продавец не вернул деньги (((	'
    
    # text_tonality(input_text=text, 
    #               preprocessing=_Preprocessing.WITHOUT_PREPROCESSING)
    
    # text_tonality(input_text=text, 
    #               preprocessing=_Preprocessing.TEXT_FORMATTING)
    
    # text_tonality(input_text=text, 
    #               preprocessing=_Preprocessing.LOGICAL_PARTS, object_review_size=3)
    
    texts = pd.read_csv('data/phone.csv').dropna()['text'].to_list()
    
    processing_functions.processing_with_buffer_reset(proc_fun=processing_functions.processing_logical_parts_dataset,
                                                      texts=texts,
                                                      output_path='data/res/phone_log_parts.csv',
                                                      object_review_size=4)