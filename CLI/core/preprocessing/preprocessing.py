if __name__ == '__main__':
    
    from logical_parts.split_to_logical_parts import split_to_logical_parts
    from text_clear import text_clear
    
else:
    
    from .logical_parts.split_to_logical_parts import split_to_logical_parts
    from .text_clear import text_clear
    
def preprocessing(text: str) -> list[str]:
    """
        Drop space and punctuation, split to logical parts
    """
    
    text = text_clear(text)
    
    text = split_to_logical_parts(text)
    
    return text


if __name__ == '__main__':
    # TEST

    print(preprocessing('В целом отель понравился номер был просторный но убирали редко было грязно в остальном все хорошо завтрак понравился'))