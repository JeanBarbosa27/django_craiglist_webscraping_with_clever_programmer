import re

from django.shortcuts import render
from bs4 import BeautifulSoup
from requests import get
from requests.compat import quote_plus

from .models import Search

# For now I'll just follow with the same URL done in the video and after I'll try make it dynamic
BASE_CRAIGLIST_SEARCH_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

def home(request):
    return render(request, 'craiglist_webscraping/base.html')

def new_search(request):
    search = request.POST['search'] if request.method == 'POST' else ''
    # Search.objects.create(search=search)

    search_url = BASE_CRAIGLIST_SEARCH_URL.format(quote_plus(search))
    response = get(search_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    final_postings = []

    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        post_price = post.find(class_='result-price').text if post.find(class_='result-price') else 'to match'
        if post.find(class_='result-image'):
            post_image_ids = str(post.find(class_='result-image').get('data-ids')).split(',')
            post_image_url = re.sub(r'\d:', '', post_image_ids[0])
            post_image = BASE_IMAGE_URL.format(post_image_url)
        else:
            post_image = 'http://via.placeholder.com/404x250'

        final_postings.append((post_title, post_url, post_price, post_image))

    context = {
        'search': search,
        'final_postings': final_postings,
    }
    return render(request, 'craiglist_webscraping/new_search.html', context)
