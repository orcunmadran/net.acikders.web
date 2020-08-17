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
        "title":request.POST.get('title'),
        "subject":request.POST.get('subject'),
        "description":request.POST.get('description'),
        "type":request.POST.get('type'),
        "creator":request.POST.get('creator'),
        "publisher":request.POST.get('publisher'),
        "contributor":request.POST.get('contributor'),
        "license":request.POST.get('license'),
        "ccLicenseURL": request.POST.get('ccLicenseURL'),
        "ccLicenseIcon": request.POST.get('ccLicenseIcon'),
        "date":request.POST.get('date'),
        "language":request.POST.get('language'),
        "format":request.POST.get('format'),
        "identifier":request.POST.get('identifier'),
        "educationalAudience":request.POST.get('educationalAudience'),
        "educationalUse":request.POST.get('educationalUse'),
        "interactivityType":request.POST.get('interactivityType'),
        "learningResourceType":request.POST.get('learningResourceType'),
        "timeRequired":request.POST.get('timeRequired')
    }
    return render(request, 'metadata.html', formveri)

def auto_view(request, *args, **kwargs):
    return render(request, 'auto.html')

def basic_view(*args, **kwargs):
    return HttpResponse("<h1>TEST</h1><p><a href='javascript:history.back()'>Geri dön...</a></p>")