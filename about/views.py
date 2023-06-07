from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'judul':'About Django',
        'kontributor':'abi',
        'nav' : [
            ['/','Home'],
            ['/about/cerita','Cerita'],
            ['/about/news','News'],
        ],
        'banner':'about/img/banner_about.jpg',
        'app_css':'about/css/styles.css'
    }
    return render(request, 'index.html', context)

def news(request):
    return HttpResponse('news about')
def cerita(request):
    return HttpResponse('cerita about')