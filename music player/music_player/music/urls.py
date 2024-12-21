from django.urls import path
from .views import *

urlpatterns = [
    path('',MusicListCreateView.as_view(),name='music-list-create'),
    path('<int:pk>/',MusicDetailView.as_view(),name='detail-list')
]