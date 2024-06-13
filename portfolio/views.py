from django.shortcuts import render


def index(request):
    context = {
        "title": "Variety V1.0"
    }
    return render(request, 'portfolio/home_page.html', context)
