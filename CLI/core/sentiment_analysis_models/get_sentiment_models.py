if __name__ == '__main__':
    
    from rubert_base_cased.rubert_base_cased_model_getter import get_rubert_base_cased
    from rubert_base_cased_blanchefort.rubert_base_cased_blanchefort_model_getter import get_rubert_base_cased_blanchefort

    
else:
    from .rubert_base_cased.rubert_base_cased_model_getter import get_rubert_base_cased
    from .rubert_base_cased_blanchefort.rubert_base_cased_blanchefort_model_getter import get_rubert_base_cased_blanchefort
    
def get_all_sentiment_models():
    
    get_rubert_base_cased()
    get_rubert_base_cased_blanchefort()
