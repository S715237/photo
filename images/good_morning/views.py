from django.shortcuts import render
from .models import GoodMorning

def morning_gallery(request):
    images = GoodMorning.objects.all()
    return render(request, 'morning_gallery.html', {'images': images})

# Create your views here.
