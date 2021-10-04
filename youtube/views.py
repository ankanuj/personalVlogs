from django.shortcuts import render

def youtubePage(request):
    return render(request, 'youtube/youtubeVideosPage.html')

