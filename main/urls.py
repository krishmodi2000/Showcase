from django.urls import path
from django.contrib.auth.decorators import login_required

from main import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('search_movies/', views.SearchMovies, name = 'search_movies'),
    path('search_tv/', views.SearchTv, name = 'search_tv'),
    path('search_person/', views.SearchPerson, name = 'search_person'),
    path('details_movies/<id>', views.DetailsMovie, name = 'details_movies'),
    path('details_tv/<id>', views.DetailsTv, name = 'details_tv'),
    path('details_person/<id>', views.DetailsPerson, name = 'details_person')
]