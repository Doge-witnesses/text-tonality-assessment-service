from sentiment_analysis_models import predictor
from object_review_models.compression import compressor 

def main():
    
    print('\n')
    
    text = 'Очень плохое качество. Сшито кое как, криво. Снаружи торчит внутренняя подкладка, внутри ни один шов не обработан. Ужас.. Мягкая, тонкая,   на ощупь приятная и цвет как на фото. Но качество пошива просто кошмар'

    print('Text:', text)
    print('\n')
    print('Sentiment:', predictor.predict(text))
    print('Object (small):', compressor.compress(text, 3))
    print('Object (medium):', compressor.compress(text, len(text.split())/2 ))
    print('Object (auto):', compressor.compress(text))
    print('\n')
    
main()