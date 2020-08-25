from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html')

def form_view(request, *args, **kwargs):
    return render(request, 'form.html')

def senddata_view(request, *args, **kwargs):
    return render(request, 'senddata.html')

def getdata_view(request, *args, **kwargs):
    formveri = {
        "title":request.GET.get('title'),
        "subject":request.GET.get('subject'),
        "learningResourceType":request.GET.get('sonuc'),
    }
    return render(request, 'getdata.html', formveri)

def metadata_view(request, *args, **kwargs):
    formveri = {
        "title":request.POST.get('title'), #1
        "subject":request.POST.get('subject'), #2
        "description":request.POST.get('description'), #3
        "type":request.POST.get('type'), #4
        "creator":request.POST.get('creator'), #5
        "publisher":request.POST.get('publisher'), #6
        "contributor":request.POST.get('contributor'), #7
        "license":request.POST.get('license'), #8
        "ccLicenseURL": request.POST.get('ccLicenseURL'),
        "ccLicenseIcon": request.POST.get('ccLicenseIcon'),
        "date":request.POST.get('date'), #9
        "language":request.POST.get('language'), #10
        "format":request.POST.get('format'), #11
        "identifier":request.POST.get('identifier'), #12
        "educationalAudience":request.POST.get('educationalAudience'), #13
        "educationalUse":request.POST.get('educationalUse'), #14
        "interactivityType":request.POST.get('interactivityType'), #15
        "timeRequired":request.POST.get('timeRequired') #16
    }
    return render(request, 'metadata.html', formveri)

def auto_view(request, *args, **kwargs):
    return render(request, 'auto.html')

def basic_view(*args, **kwargs):
    return HttpResponse("<h1>TEST</h1><p><a href='javascript:history.back()'>Geri dön...</a></p>")