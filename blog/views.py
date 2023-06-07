# views blog

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'judul':'Blog Django',
        'kontributor':'abi',
        'nav' : [
            ['/','Home'],
            ['/blog/cerita','Cerita'],
            ['/blog/news','News'],
        ],
        'banner':'blog/img/banner_blog.jpg',
        'app_css':'blog/css/styles.css'
    }
    return render(request, 'index.html', context)
def news(request):
    context = {
        'judul':'news Django',
        'kontributor':'bilal'
    }
    return render(request, 'blog/index.html', context)
def cerita(request):
    context = {
        'judul':'cerita Django',
        'kontributor':'ismail'
    }
    return render(request, 'blog/index.html', context)
