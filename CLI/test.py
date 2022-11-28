if __name__ == '__main__':

    from core import processing_functions
    
else:
    
    from .core import processing_functions

from enum import Enum

class _Preprocessing(Enum):
    
    WITHOUT_PREPROCESSING = 0
    TEXT_FORMATTING = 1
    LOGICAL_PARTS = 2



def text_tonality(preprocessing: _Preprocessing, text, object_review_size: int = 5):
    """Evaluation of tonality for input text"""
    
    if preprocessing == _Preprocessing.WITHOUT_PREPROCESSING:
        processed_text = processing_functions.processing_text(text, object_review_size).unwrappe()
        
        print('=' * 100, '\n')
        print(f'\tTEXT: \"{processed_text[0]}\"\n\tSENTIMENT: {processed_text[1]}\n\tOBJECT: {processed_text[2]}\n')
        print('=' * 100)
        
    elif preprocessing == _Preprocessing.TEXT_FORMATTING:
        processed_text = processing_functions.processing_formatted_text(text, object_review_size).unwrappe()
        
        print('=' * 100, '\n')
        print(f'\tTEXT: \"{processed_text[0]}\"\n\tSENTIMENT: {processed_text[1]}\n\tOBJECT: {processed_text[2]}\n')
        print('=' * 100)
        
    elif preprocessing == _Preprocessing.LOGICAL_PARTS:
        processed_logical_parts = processing_functions.processing_logical_parts(text, object_review_size).unwrappe_to_list()

        for part_id in range(len(processed_logical_parts)):
            print('=' * 100, '\n')
            print(f'\tPART {part_id + 1}: \"{processed_logical_parts[part_id][0]}\"\n\tSENTIMENT: {processed_logical_parts[part_id][1]}\n\tOBJECT: {processed_logical_parts[part_id][2]}\n')
            print('=' * 100)
    
if __name__ == '__main__':
    
    text = 'Повязка пришла вовремя ,   но вся драная . Очень жаль.'
    
    text_tonality(text=text, 
                  preprocessing=_Preprocessing.WITHOUT_PREPROCESSING)
    
    text_tonality(text=text, 
                  preprocessing=_Preprocessing.TEXT_FORMATTING)
    
    text_tonality(text=text, 
                  preprocessing=_Preprocessing.LOGICAL_PARTS, object_review_size=3)