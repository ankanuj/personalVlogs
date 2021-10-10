from django.shortcuts import render

def healthAndFitnessPage(request):
    return render(request, 'healthAndFitness/healthAndFitness.html')

def dedicatedBlogPage(request):
    return render(request, 'healthAndFitness/dedicatedBlogPage.html')

