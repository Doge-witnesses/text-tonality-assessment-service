if __name__ == '__main__':
    
    from logical_parts.split_to_logical_parts import split_to_logical_parts
    from text_clear import text_clear
    
else:
    
    from .logical_parts.split_to_logical_parts import split_to_logical_parts
    from .text_clear import text_clear
    
def preprocessing1(text: str) -> list[str]:
    """
        Split to logical parts, drop space and punctuation
    """
    
    log_parts = split_to_logical_parts(text)
    
    print(log_parts)
    
    for part_id in range(len(log_parts)):
        log_parts[part_id] = text_clear(log_parts[part_id])
    
    return log_parts

def preprocessing2(text: str) -> list[str]:
    """
        Drop space and punctuation, split to logical parts
    """
    
    text = text_clear(text)
    
    log_parts = split_to_logical_parts(text)
    
    return log_parts


def preprocessing3(text: str) -> list[str]:
    """
        ...
    """
    log_parts = split_to_logical_parts(text)
    
    return log_parts
    

if __name__ == '__main__':
    # TEST

    print(preprocessing1('В целом отель понравился номер был просторный но убирали редко было грязно в остальном все хорошо завтрак понравился'))