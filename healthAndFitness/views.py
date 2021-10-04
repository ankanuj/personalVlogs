from django.shortcuts import render

def healthAndFitnessPage(request):
    return render(request, 'healthAndFitness/healthAndFitness.html')

