
if __name__ == '__main__':
    
    #from rubert_base_cased.rubert_base_cased_model import rubert_base_cased_predict
    from rubert_base_cased_blanchefort.rubert_base_cased_blanchefort_model import rubert_base_cased_blanchefort_predict

else:
    
    #from .rubert_base_cased.rubert_base_cased_model import rubert_base_cased_predict
    from .rubert_base_cased_blanchefort.rubert_base_cased_blanchefort_model import rubert_base_cased_blanchefort_predict


def predict(text: str, predictor = rubert_base_cased_blanchefort_predict) -> int:
    """
    [0] -   NEG;
    [1] -   POS;
    [2] -   NEG;
    """

    return int(predictor(text))
