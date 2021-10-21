from django.urls import path
from . import views

urlpatterns = [
    path('health/and/fitness', views.healthAndFitnessPage, name='healthAndFitness'),
    path('health/and/fitness/blogs/{?P<pk>\d+}', views.dedicatedBlogPage, name='blogPage'),
]