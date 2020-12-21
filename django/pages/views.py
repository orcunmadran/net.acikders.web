from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html')

def test_view(request, *args, **kwargs):
    return render(request, 'test.html')

def form_view(request, *args, **kwargs):
    return render(request, 'metaform.html')

def sema_view(request, *args, **kwargs):
    return render(request, 'schema.html')

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
        "accesibilityFeature":request.POST.get('accesibilityFeature'), #15
        "timeRequired":request.POST.get('timeRequired') #16
    }
    return render(request, 'metadata.html', formveri)

def database_view(request, *args, **kwargs):
    formveri2 = {
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
        "accesibilityFeature":request.POST.get('accesibilityFeature'), #15
        "timeRequired":request.POST.get('timeRequired') #16
    }
    '''
    # SQLite3 kütüphanesi yükleniyor
    import sqlite3
    # veritabani.db adında bir SQLite3 veri tabanı dosyası oluşturuluyor.
    veritabani = sqlite3.connect('db.sqlite3')
    # Veri tabanı üzerinde işlemleri gerçekleştirebilmek için bir Cursor objesi oluşturuluyor.
    komut = veritabani.cursor()
    # Veri tabanındaki tabloları görüntüle
    komut.execute("INSERT INTO oers_oersTest (oer_name, oer_url, oer_types) VALUES (?,?,?)", (request.POST.get('title'), request.POST.get('identifier'), request.POST.get('type')))
    veritabani.commit()
    '''
    return render(request, 'database.html', formveri2)

def basic_view(*args, **kwargs):
    return HttpResponse("<h1>TEST</h1><p><a href='javascript:history.back()'>Geri dön...</a></p>")