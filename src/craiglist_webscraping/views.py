from django.shortcuts import render
from bs4 import BeautifulSoup

from requests import get
from requests.compat import quote_plus


# For now I'll just follow with the same URL done in the video and after I'll try make it dynamic
BASE_CRAIGLIST_SEARCH_URL = 'https://losangeles.craigslist.org/search/?query={}'

def home(request):
    return render(request, 'craiglist_webscraping/base.html')

def new_search(request):
    search = request.POST['search']
    search_url = BASE_CRAIGLIST_SEARCH_URL.format(quote_plus(search))
    response = get(search_url)
    data = response.text

    context = {
        'search': search,
    }
    return render(request, 'craiglist_webscraping/new_search.html', context)
