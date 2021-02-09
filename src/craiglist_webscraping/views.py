from django.shortcuts import render

def home(request):
    return render(request, 'craiglist_webscraping/base.html')

def new_search(request):
    return render(request, 'craiglist_webscraping/new_search.html')
