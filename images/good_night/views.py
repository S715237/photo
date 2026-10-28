from django.shortcuts import render
from .models import GoodNight,Diwali, christmas,krishnaJanmashtmi, Ganeshchathurthi, Navratri,Login
from .forms import LoginForm


def good_night_view(request):
    good_night_images = GoodNight.objects.all()
    return render(request, 'good_night.html', {'good_night_images': good_night_images})

def diwali_views(request):
    abc = Diwali.objects.all()
    return render (request,'diwali.html',{'data':abc})


def krishna_view(request):
    data = krishnaJanmashtmi.objects.all()
    return render(request, 'krishna.html', {'data': data})

def ganesh_view(request):
    data = Ganeshchathurthi.objects.all()
    return render(request, 'ganesh.html', {'data': data})

def navratri_view(request):
    data = Navratri.objects.all()
    return render(request, 'navratri.html', {'data': data})

def christmas_view(request):    
    data = christmas.objects.all()
    return render(request, 'christmas.html', {'data': data})

def showform(request):
    if request.method == "POST":
        fm = LoginForm(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            ps = fm.cleaned_data['password']

            register = Login(name=nm, email=em, password=ps)
            register.save()
             
    else:
        fm=LoginForm() 
    return render(request, 'showform.html', {'form':fm})






