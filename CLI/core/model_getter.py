if __name__ == '__main__':

    from object_review_models.get_object_review_models import get_all_object_review_models
    from sentiment_analysis_models.get_sentiment_models import get_all_sentiment_models

else:
    
    from .object_review_models.get_object_review_models import get_all_object_review_models
    from .sentiment_analysis_models.get_sentiment_models import get_all_sentiment_models
    
def get_all_models():
    
    get_all_object_review_models()
    get_all_sentiment_models()
    
    
if __name__ == '__main__':
    get_all_models()
