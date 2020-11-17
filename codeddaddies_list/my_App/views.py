import requests
from urllib.parse import quote_plus  # spaces are converted to +
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models



BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'

def home(request):
    return render(request, 'base.html')


def new_search(request):
    # get in dictionary in python
    search = request.POST.get('search')
    # create search objects
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    # parser html data(read html data) in soup object .
    soup = BeautifulSoup(data, 'html.parser')

    # a is link. find all the links where the class is result-title (class="result-title hdrlnk")
    # BeautifulSoup version 4.9.0 soup.find_all('a', class_='result-title' )
    post_listings = soup.find_all('li', class_='result-row' )

    final_postings = []
    for post in post_listings:

        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        final_postings.append((post_title, post_url, post_price))

    stuff_for_frontend = {
        'search' : search,
        'final_postings' : final_postings,
    }
    return render(request, 'my_App/new_search.html', stuff_for_frontend)