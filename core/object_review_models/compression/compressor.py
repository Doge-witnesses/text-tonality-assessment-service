from ..compression.model_rubert_tiny2_sentence_compression import model as RT2_model


def compress(text, compressor = RT2_model.rubert_tiny2_compress):
    # (str, function) -> str
    return compressor(text, keep_ratio=min(0.99, 5/len(text.split())))
