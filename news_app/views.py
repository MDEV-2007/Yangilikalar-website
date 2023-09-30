from django.shortcuts import redirect, HttpResponse, render, get_object_or_404
from .models import *
from django.views.generic import UpdateView, ListView, DeleteView,CreateView
from .forms import ContactForm
from django.urls import reverse_lazy

def news_list(request):
    # news_list = New.objects.filter(status=New.Status.Published)
    news_list = New.published.all()
    
    return render(request, "news/news_list.html", {
        'news_list':news_list
    })
    
    
def news_detail(request, news):
    news = get_object_or_404(New,slug=news,status=New.Status.Published)
    
    return render(request, 'news/news_detail.html',{
        'news':news
    })
    
def HomePage(request):
    mahaliy_new = New.published.all().filter(category__name='Mahaliy')[:5]
    sport_news = New.published.all().filter(category__name='Sport')[:5]
    texnologiya_new = New.published.all().filter(category__name='Texnologiya')[:5]
    xorij_new = New.published.all().filter(category__name='Xorijiy')[:5]
    iqtisod_new = New.published.all().filter(category__name='Iqtisodiyot')[:2]
    biznes_new = New.published.all().filter(category__name='Biznes')
    news_list = New.published.all().order_by('-publish_time')[:6]
    categoryies = Category.objects.all()
    categ  = Category.objects.all()[:4]
    
    return render(request, 'news/home.html',{
        'news_list':news_list,
        'categoryies':categoryies,
        'categ':categ,
        'mahaliy_new':mahaliy_new,
        'sport_news':sport_news,
        'texnologiya_new':texnologiya_new,
        'xorij_new':xorij_new,
        'iqtisod_new':iqtisod_new,
        'biznes_new':biznes_new
    })
    
def contactPageview(request):
    # print(request.POST)
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home_page')
    
    return render(request, 'news/contact.html',{
        'form':form
    })
    
class LocalNewView(ListView):
    model = New
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_yangiliklar'
    
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Mahaliy')
        return news
    
    
class XorijView(ListView):
    model = New
    template_name = 'news/xorij.html'
    context_object_name = 'xorijiy_yangiliklar'
    
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Xorijiy')
        return news
    
    
class TexnologiyaNewView(ListView):
    model = New
    template_name = 'news/texnologiya.html'
    context_object_name = 'texnologiya_yangiliklar'
    
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Texnologiya')
        return news
    

class SportNewView(ListView):
    model = New
    template_name = 'news/sport.html'
    context_object_name = 'sport_yangiliklar'
    
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')
        return news
    
    
    
class IqtisodNewView(ListView):
    model = New
    template_name = 'news/iqtisod.html'
    context_object_name = 'iqtisod_yangiliklar'
    
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Iqtisodiyot')
        return news
    
class NewsUpdateView(UpdateView):
    model = New
    fields = ('title', 'body','image','category','status')
    template_name = 'crud/news_edit.html'



class DeleteView(DeleteView):
    model = New
    template_name = 'crud/news_delete.html' 
    success_url = reverse_lazy('home_page')



class NewsCreateView(CreateView):
    model = New
    template_name = 'crud/news_create.html'
    fields = ('title', 'slug','body','image','category','status')