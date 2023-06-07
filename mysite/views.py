from django.http import HttpResponse
from django.shortcuts import render

# method view
def index(request):
    context = {
        'judul' : 'belajar Django',
        'kontributor' : 'abi',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
            ['/contact','Contact'],
        ],
        'banner':'img/banner_home.jpg'
    }
    return render(request, 'index.html', context)
