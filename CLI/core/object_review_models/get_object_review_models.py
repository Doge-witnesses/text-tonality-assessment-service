if __name__ == '__main__':
    
    from compression.model_rubert_tiny2_sentence_compression.model_rubert_tiny2_sentence_compression_getter import get_rubert_tiny2_sentence_compression
    
else:
    from .compression.model_rubert_tiny2_sentence_compression.model_rubert_tiny2_sentence_compression_getter import get_rubert_tiny2_sentence_compression

    def get_all_object_review_models() -> None:
        
        get_rubert_tiny2_sentence_compression()