'''Defines URL patterns for learning_diary logs.'''

from django.urls import path
from . import views

app_name = 'learning_diary'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
