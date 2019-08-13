from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView

from main import models

class Index(TemplateView):
    template_name = 'main/index.html'

