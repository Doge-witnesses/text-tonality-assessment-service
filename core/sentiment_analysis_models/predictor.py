from .rubert_base_cased import model as rubert


def predict(text, predictor = rubert.rubert_base_cased):
    # (str, function) -> str
    predict = int(predictor(text))
    
    
    if (predict == 0):
        return 'NEUTRAL'
    elif (predict == 1):
        return 'POSITIVE'
    else:
        return 'NEGATIVE'
