from django.shortcuts import render
from .models import moviews,molly

def showmoviews(request):
    abc = moviews.objects.all()
    return render(request, 'movie.html', {'data':abc})

def showmolly(request):
    abc = molly.objects.all()
    return render(request, 'molly.html', {'data':abc})
# Create your views here.
