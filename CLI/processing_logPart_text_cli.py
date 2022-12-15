import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import click

@click.command()
@click.option('-ORS', type=int, default=0, show_default=True, help="""Number of words in object review""")
@click.argument('text', type = click.STRING)
def processing(ors, text):
    from core import processing_functions
    
    processed_text = processing_functions.processing_logical_parts(text, ors)

    _processed_parts = processed_text.processed_texts
    
    for _processed_part_id in range(len(_processed_parts)):
        
        print('=' * 100, '\n')
        print(f'\tPART {_processed_part_id + 1}: \"{_processed_parts[_processed_part_id].text}\"\n\tSENTIMENT: {_processed_parts[_processed_part_id].sentiment.name}\n\tOBJECT: {_processed_parts[_processed_part_id].object_review}\n')
        print('=' * 100)
        
if __name__ == '__main__':
    processing()
