def text_clear(text : str) -> str:
    """
        Clearing the text
    """
    
    for letter in text:
        x = ord(letter)
        if (x >= 1072 and x <= 1103) or (x >= 1040 and x <= 1071) or x == 1105 or x == 1025 or x == 32:
            continue
        else:
            text = text.replace(letter, ' ')
            
    while '  ' in text:
        text = text.replace('  ', ' ')
    if text[len(text)-1] == ' ':
        text = text[:len(text)-1]
            
    return text
