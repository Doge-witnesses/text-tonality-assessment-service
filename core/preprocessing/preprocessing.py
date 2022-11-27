if __name__ == '__main__':
    
    from logical_parts.split_to_logical_parts import split_to_logical_parts
    from formatting.punctuation import drop_space_and_punctuation
    
else:
    
    from .logical_parts.split_to_logical_parts import split_to_logical_parts
    from .formatting.punctuation import drop_space_and_punctuation
    
def preprocessing(text):
    # (str) -> list[str]
    
    text = drop_space_and_punctuation(text)
    
    text = split_to_logical_parts(text)
    
    return text


if __name__ == '__main__':
    # TEST
    
    print(preprocessing('В целом отель понравился номер был просторный но убирали редко было грязно в остальном все хорошо завтрак понравился'))