
def drop_space_and_punctuation(text: str) -> str:

    text = text.replace('!', ' ').replace('?', ' ').replace('.', ' ').replace(',', ' ').replace('#', ' ').replace('-', ' ').replace('_', ' ').replace('\t', ' ').lower()
    
    return text.replace('  ', ' ')