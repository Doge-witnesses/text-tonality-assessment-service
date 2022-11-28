if __name__ == '__main__':

    from core import processing_functions
    
else:
    
    from .core import processing_functions

import click


@click.command()
@click.option('--preprocessing', '-PRE', type=int, default=0, show_default=True, help=
              """
              Preprocessing the source text.
              
                [0]: Without preprocessing
                [1]: Text formatting
                [2]: Splitting the text into logical parts
              """)
@click.option('--object_review_size', '-ORS', type=int, default=3, show_default=True, help=
              """
              Number of words in object review
              """)
@click.argument('text', type = click.STRING)
def text_tonality(preprocessing, object_review_size, text):
    """Evaluation of tonality for input text"""
    
    if preprocessing == 0:
        processed_text = processing_functions.processing_text(text, object_review_size).unwrappe()
        
        print('=' * 100, '\n')
        print(f'\tTEXT: \"{processed_text[0]}\"\n\tSENTIMENT: {processed_text[1]}\n\tOBJECT: {processed_text[2]}\n')
        print('=' * 100)
        
    elif preprocessing == 1:
        processed_text = processing_functions.processing_formatted_text(text, object_review_size).unwrappe()
        
        print('=' * 100, '\n')
        print(f'\tTEXT: \"{processed_text[0]}\"\n\tSENTIMENT: {processed_text[1]}\n\tOBJECT: {processed_text[2]}\n')
        print('=' * 100)
        
    elif preprocessing == 2:
        processed_texts = processing_functions.processing_logical_parts(text, object_review_size).unwrappe_to_list()

        for processed_text in processed_texts:
            print('=' * 100, '\n')
            print(f'\tTEXT: \"{processed_text[0]}\"\n\tSENTIMENT: {processed_text[1]}\n\tOBJECT: {processed_text[2]}\n')
            print('=' * 100)
    
if __name__ == '__main__':
    
    text_tonality()