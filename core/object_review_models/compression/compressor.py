from ..compression.model_rubert_tiny2_sentence_compression import model as RT2_model


def compress(text, num_words = 0, compressor = RT2_model.rubert_tiny2_compress):
    # (str, function) -> str
    if (num_words == 0):
        return compressor(text)
    
    return compressor(text, keep_ratio=min(0.99, num_words/len(text.split())))
