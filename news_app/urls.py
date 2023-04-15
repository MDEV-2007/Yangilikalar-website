from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage,name='home_page'),
    path('contact/', contactPageview,name='contact_page'),
    path('all-news/', news_list, name='all_news_list'),
    path('news_detail_page/<slug:news>/', news_detail, name='news_detail'),
    path('mahalliy/', LocalNewView.as_view(), name='mahaliy_news_page'),
    path('xorij/', XorijView.as_view(), name='xorij_news_page'),
    path('texno/', TexnologiyaNewView.as_view(), name='texno_news_page'),
    path('sport/', SportNewView.as_view(), name='sport_news_page'),
    path('iqtisod_bilimlar/', IqtisodNewView.as_view(), name='iqtisod_news_page')
]