from django.urls import path
from django.contrib.auth.decorators import login_required

from main import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
]