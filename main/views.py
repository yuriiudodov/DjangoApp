from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import first

def index(request):
    context = {
        'title':'Home',
        'content':'Главная страница магазина - HOME',
        'list': ['first', 'second'],
        'dict': {'first':1},
        'is_authenticated':False
    }
    return render(request, 'main/index.html', context) #HttpResponse('Home page')


def about(request):
    return HttpResponse('About page')
# Create your views here.
