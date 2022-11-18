from sentiment_analysis_models import predictor
from object_review_models.compression import compressor 

def main():
    
    text = input()
    
    print('Sentiment:', predictor.predict(text))
    print('Object:', compressor.compress(text))
    
main()