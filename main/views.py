from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, ListView

import json
import requests

from main import models


class Index(TemplateView):
    template_name = 'main/index.html'


class Search(TemplateView):
    template_name = 'main/search.html'


def SearchMovies(request):
    api_key = 'c4cc6806388f5424ca7bad9c0cd0440b'
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
    api_key = 'c4cc6806388f5424ca7bad9c0cd0440b'
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
    return render(request, 'main/search_movies.html', context)


def SearchPerson(request):
    api_key = 'c4cc6806388f5424ca7bad9c0cd0440b'
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


def Top10Movies(request):
    id_list = [278, 238, 240, 155, 389, 424, 122, 680, 429, 550]
    api_key = 'c4cc6806388f5424ca7bad9c0cd0440b'
    results = {}
    movie_list = []
    for i in id_list:
        url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(
            i, api_key)
        response = requests.get(url)
        results = response.json()
        movie_list.append(results)
    context = {
        'results': movie_list
    }
    return render(request, 'main/index.html', context)