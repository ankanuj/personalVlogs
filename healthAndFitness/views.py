from django.shortcuts import redirect, render
from .models import HealthAndFitnessBlog

def healthAndFitnessPage(request):
    blogs = HealthAndFitnessBlog.objects.order_by('-id')
    content = { 'blogs':blogs, }
    return render(request, 'healthAndFitness/healthAndFitness.html',content)

def dedicatedBlogPage(request,pk=None):
    if pk:
        blogs = HealthAndFitnessBlog.objects.get(pk=pk)
        content= { 'blogs':blogs,}
        return render(request, 'healthAndFitness/dedicatedBlogPage.html',content)
    else:
        redirect('index')

