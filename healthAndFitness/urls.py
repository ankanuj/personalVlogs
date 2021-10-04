from django.urls import path
from . import views

urlpatterns = [
    path('health/and/fitness', views.healthAndFitnessPage, name='healthAndFitness'),

]