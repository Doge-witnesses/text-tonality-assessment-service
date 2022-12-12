from core import processing_functions

from enum import Enum

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
    
    res = processing_functions.processing_logical_parts('Доставка быстрая.Всего 20 дней.За это и 3 звезды.Ласины очень тонкие.Совсем прозрачные.Со всех сторон просвечивают.Просто не лосины а колготки на 150-200 ден.Носить не буду. ', object_review_size=3)
    
    _processed_parts = res.processed_texts
    
    for _processed_part_id in range(len(_processed_parts)):
        
        print('=' * 100, '\n')
        print(f'\tPART {_processed_part_id + 1}: \"{_processed_parts[_processed_part_id].text}\"\n\tSENTIMENT: {_processed_parts[_processed_part_id].sentiment.name}\n\tOBJECT: {_processed_parts[_processed_part_id].object_review}\n')
        print('=' * 100)