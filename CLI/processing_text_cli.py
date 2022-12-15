import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import click

@click.command()
@click.option('-ORS', type=int, default=0, show_default=True, help="""Number of words in object review""")
@click.argument('text', type = click.STRING)
def processing(ors, text):
    from core import processing_functions
    
    processed_text = processing_functions.processing_text(text, ors)

    print('=' * 100, '\n')
    print(f'\tTEXT: \"{processed_text.text}\"\n\tSENTIMENT: {processed_text.sentiment.name}\n\tOBJECT: {processed_text.object_review}\n')
    print('=' * 100)

