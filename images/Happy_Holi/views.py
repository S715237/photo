from django.shortcuts import render
from .models import Holi

def holi_view(request):
    images = Holi.objects.all()
    return render(request, 'holi.html', {'images': images})

# Create your views here.
