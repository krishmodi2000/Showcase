from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, ListView

from django.conf import settings

import json
import requests

from main import models


class Index(TemplateView):
    template_name = 'main/index.html'


class Search(TemplateView):
    template_name = 'main/search.html'


def SearchMovies(request):
    api_key = settings.API_KEY
    results = {}
    if 'Search' in request.GET:
        query = request.GET['Search']
        url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(
            api_key, query)
        response = requests.get(url)
        results = response.json()
    context = {
        'results': results
    }
    return render(request, 'main/search_movies.html', context)


def SearchTv(request):
    api_key = settings.API_KEY
    results = {}
    if 'Search' in request.GET:
        query = request.GET['Search']
        url = 'https://api.themoviedb.org/3/search/tv?api_key={}&query={}'.format(
            api_key, query)
        response = requests.get(url)
        results = response.json()
    context = {
        'results': results
    }
    return render(request, 'main/search_tv.html', context)


def SearchPerson(request):
    api_key = settings.API_KEY
    results = {}
    if 'Search' in request.GET:
        query = request.GET['Search']
        url = 'https://api.themoviedb.org/3/search/person?api_key={}&query={}'.format(
            api_key, query)
        response = requests.get(url)
        results = response.json()
    context = {
        'results': results
    }
    return render(request, 'main/search_person.html', context)


def DetailsMovie(request, id):
    api_key = settings.API_KEY
    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(
        id, api_key)
    response1 = requests.get(url)
    results = response1.json()

    url = 'https://api.themoviedb.org/3/movie/{}/similar?api_key={}'.format(
        id, api_key)
    response2 = requests.get(url)
    similar = response2.json()

    url = 'https://api.themoviedb.org/3/movie/{}/credits?api_key={}'.format(
        id, api_key)
    response3 = requests.get(url)
    creds = response3.json()

    url = 'https://api.themoviedb.org/3/movie/{}/videos?api_key={}'.format(
        id, api_key)
    response4 = requests.get(url)
    vids = response4.json()

    context = {
        'results': results,
        'credits': creds,
        'similar': similar,
        'videos': vids
    }
    return render(request, 'main/details_movies.html', context)


def DetailsTv(request, id):
    api_key = settings.API_KEY
    url = 'https://api.themoviedb.org/3/tv/{}?api_key={}'.format(
        id, api_key)
    response = requests.get(url)
    results = response.json()

    url = 'https://api.themoviedb.org/3/tv/{}/similar?api_key={}'.format(
        id, api_key)
    response2 = requests.get(url)
    similar = response2.json()

    url = 'https://api.themoviedb.org/3/tv/{}/credits?api_key={}'.format(
        id, api_key)
    response3 = requests.get(url)
    creds = response3.json()

    url = 'https://api.themoviedb.org/3/tv/{}/videos?api_key={}'.format(
        id, api_key)
    response4 = requests.get(url)
    vids = response4.json()

    context = {
        'results': results,
        'credits': creds,
        'similar': similar,
        'videos': vids
    }
    return render(request, 'main/details_tv.html', context)


def DetailsPerson(request, id):
    api_key = settings.API_KEY

    url = 'https://api.themoviedb.org/3/person/{}?api_key={}'.format(
        id, api_key)
    response = requests.get(url)
    results = response.json()


    url = 'https://api.themoviedb.org/3/person/{}/combined_credits?api_key={}'.format(
        id, api_key)
    response3 = requests.get(url)
    creds = response3.json()

    context = {
        'results': results,
        'credits': creds
    }
    return render(request, 'main/details_person.html', context)
