
if __name__ == '__main__':
    
    from rubert_base_cased.rubert_base_cased_model import rubert_base_cased_predict
    from rubert_base_cased_blanchefort.rubert_base_cased_blanchefort_model import rubert_base_cased_blanchefort_predict

else:
    
    from .rubert_base_cased.rubert_base_cased_model import rubert_base_cased_predict
    from .rubert_base_cased_blanchefort.rubert_base_cased_blanchefort_model import rubert_base_cased_blanchefort_predict


def predict(text, predictor = rubert_base_cased_blanchefort_predict):
    # (str, function) -> str
    predict = int(predictor(text))
    
    
    if (predict == 0):
        return 'NEUTRAL'
    elif (predict == 1):
        return 'POSITIVE'
    else:
        return 'NEGATIVE'
