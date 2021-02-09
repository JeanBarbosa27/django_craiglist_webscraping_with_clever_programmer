from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('search-results', new_search, name='new_search'),
]
