from django.shortcuts import render

def home(request):
    return render(request, 'craiglist_webscraping/base.html')
