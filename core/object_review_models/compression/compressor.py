if __name__ == '__main__':
    
    from model_rubert_tiny2_sentence_compression.model_rubert_tiny2_sentence_compression import rubert_tiny2_compress

else:
    
    from .model_rubert_tiny2_sentence_compression.model_rubert_tiny2_sentence_compression import rubert_tiny2_compress
    

def compress(text, num_words = 0, compressor = rubert_tiny2_compress):
    # (str, function) -> str
    if (num_words == 0):
        return compressor(text)
    
    return compressor(text, keep_ratio=min(0.999999999, (num_words + 1)/(len(text.split()) + 1)))
