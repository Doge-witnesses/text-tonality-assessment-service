if __name__ == '__main__':
    
    from model_rubert_tiny2_sentence_compression.model_rubert_tiny2_sentence_compression import rubert_tiny2_compress

else:
    
    from .model_rubert_tiny2_sentence_compression.model_rubert_tiny2_sentence_compression import rubert_tiny2_compress
    

def compress(text: str, num_words: int = 0, compressor = rubert_tiny2_compress) -> str:

    if (num_words == 0):
        return compressor(text)
    
    coef = (num_words + 1)/len(text.split())
    
    if coef >= 1:
        return text
    
    return compressor(text, keep_ratio=coef)
