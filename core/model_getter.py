from object_review_models import get_all_models as ORM_getter
from sentiment_analysis_models import get_all_models as SAM_getter

def main():
    ORM_getter.main()
    SAM_getter.main()
    
main()
