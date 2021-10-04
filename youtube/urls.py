from django.urls import path
from . import views

urlpatterns = [
    path('anuj/youtube/videos', views.youtubePage, name='youtubePage'),

]