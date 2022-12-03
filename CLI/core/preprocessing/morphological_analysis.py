import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def word_normalization(word: str) -> str:
    """
        Word normalization
    """
    
    ans = morph.parse(word)[0]
    return ans.normal_form


def text_normalization(text: str) -> str:
    
    words = text.split(' ')
    
    for word_it in range(len(words)):
        
        words[word_it] = word_normalization(words[word_it])
        
    return ' '.join(words)