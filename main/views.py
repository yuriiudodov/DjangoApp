from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import first

def index(request):
    context = {
        'title':'Home - Главная',
        'content':'Магазин мебели HOME'
        
    }

    return render(request, 'main/index.html', context) #HttpResponse('Home page')


def about(request):
    context = {
        'title':'Home - О Нас',
        'content':'О нас',
        'text_on_page':'уээээ странный текст'
        
    }

    return render(request, 'main/about.html', context) #HttpResponse('Home page')
# Create your views here.
