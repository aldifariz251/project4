from django.shortcuts import render, redirect
from .models import Motor

# from django.http import HttpResponse
# from .models import motor

# Create your views here.
def Index(request):
    return render(request, "index.html")

def TambahDaftarMotor(request):
    return render(request, "tambahmotor.html")

def Create(request):
    if request.method=="POST":
        nama =request.POST.get('nama')
        merk =request.POST.get('merk')
        plat =request.POST.get('plat')
        telp =request.POST.get('telp')
        email =request.POST.get('email')

        
        obj = Motor.objects.create(nama= nama, merk= merk, plat= plat, telp= telp, email= email)
        obj.save()
        return redirect('/tambahdaftarmotor')

def Login(request):
    return render(request, "login.html")

def Register(request):
    return render(request, "register.html")