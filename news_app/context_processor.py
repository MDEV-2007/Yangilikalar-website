from .models import New

def latest_news(request):
    latest_news = New.published.all().order_by("-publish_time")[:10]
    
    context = {
        'latest_news':latest_news
    }
    return context