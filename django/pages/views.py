from django.http import HttpResponse
from django.shortcuts import render
from .models import OerData
import sqlite3
import datetime
import mlModel

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html')

def about_view(request, *args, **kwargs):
    return render(request, 'about.html')

def schema_view(request, *args, **kwargs):
    return render(request, 'schema.html')

def app01_view(request, *args, **kwargs):
    return render(request, 'app01.html')

def app02_view(request, *args, **kwargs):
    return render(request, 'app02.html')

def metaform_view(request, *args, **kwargs):
    return render(request, 'metaform.html')

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
        "accessibilityFeature":request.POST.get('accessibilityFeature'), #15
        "timeRequired":request.POST.get('timeRequired') #16
    }
    return render(request, 'metadata.html', formveri)

def metabase_view(request, *args, **kwargs):

    # veritabani.db adında bir SQLite3 veri tabanı dosyası oluşturuluyor.
    veritabani = sqlite3.connect('db.sqlite3')
    # Veri tabanı üzerinde işlemleri gerçekleştirebilmek için bir Cursor objesi oluşturuluyor.
    komut = veritabani.cursor()
    # Veri tabanındaki tabloları görüntüle
    komut.execute("INSERT INTO pages_OerData(oer_auto_date, oer_title, oer_subject, oer_description, oer_type, oer_creator, oer_publisher, oer_contributor, oer_license, oer_date, oer_language, oer_format, oer_identifier, oer_educationalAudience, oer_educationalUse, oer_accessibilityFeature, oer_timeRequired) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        datetime.datetime.utcnow(),
                        request.POST.get('title'),
                        request.POST.get('subject'),
                        request.POST.get('description'),
                        request.POST.get('type'),
                        request.POST.get('creator'),
                        request.POST.get('publisher'),
                        request.POST.get('contributor'),
                        request.POST.get('license'),
                        request.POST.get('date'),
                        request.POST.get('language'),
                        request.POST.get('format'),
                        request.POST.get('identifier'),
                        request.POST.get('educationalAudience'),
                        request.POST.get('educationalUse'),
                        request.POST.get('accessibilityFeature'),
                        request.POST.get('timeRequired')
                    )
                  )
    veritabani.commit()

    # Veri tabanı bağlantısı kapatılıyor
    veritabani.close()

    return render(request, 'metabase.html')

def basic_view(*args, **kwargs):
    return HttpResponse("<h1>TEST</h1><p><a href='javascript:history.back()'>Geri dön...</a></p>")

def search_view(request):

    q = request.GET.get('q')
    keywords = q.split()

    # Standart Query
    queryString = ""
    for keydata in keywords:
        queryString += '''(
                        OE.oer_title LIKE '%{keyword}%' OR 
                        OE.oer_subject LIKE '%{keyword}%' OR 
                        OE.oer_description LIKE '%{keyword}%' OR
                        OE.oer_creator LIKE '%{keyword}%' OR
                        OE.oer_publisher LIKE '%{keyword}%' OR 
                        OE.oer_contributor LIKE '%{keyword}%') AND '''.format(keyword = keydata)

    rows = OerData.objects.raw('''
        SELECT OE.*, LI.*, SUBSTR(OE.oer_description,0,75) AS summary
        FROM pages_OerData OE, pages_LicenseData LI
        WHERE {query} OE.oer_license = LI.license_code
        '''.format(query = queryString))
    rowstotal = (len(rows))

    #ML Query
    myModel = mlModel
    kelimeVektoru = myModel.kelimeVektoru
    aranacakKelimeler = []
    cikartilanKelimeler = []

    for kelime in keywords:
        if kelime in kelimeVektoru:
            aranacakKelimeler.append(kelime)
        else:
            cikartilanKelimeler.append(kelime)
    print("- - - - -")
    print("Aranacak Kelimeler : " + str(aranacakKelimeler))
    print("Çıkartılan Kelimeler : " + str(cikartilanKelimeler))

    if len(aranacakKelimeler) > 0:
        oneriler = (kelimeVektoru.most_similar(positive=aranacakKelimeler))
        print(oneriler)
        sorguCumlesi = ""
        oneriListesi = []
        for oneri in oneriler:
            sorguCumlesi += '''
                            OE.oer_title LIKE '%{anahtar}%' OR 
                            OE.oer_subject LIKE '%{anahtar}%' OR 
                            OE.oer_description LIKE '%{anahtar}%' OR
                            OE.oer_creator LIKE '%{anahtar}%' OR
                            OE.oer_publisher LIKE '%{anahtar}%' OR 
                            OE.oer_contributor LIKE '%{anahtar}%' OR '''.format(anahtar = oneri[0])
            oneriListesi.append(oneri[0])

        rows2 = OerData.objects.raw('''
            SELECT OE.*, LI.*, SUBSTR(OE.oer_description,0,75) AS summary
            FROM pages_OerData OE, pages_LicenseData LI
            WHERE ({query} OE.oer_contributor = 'X') AND OE.oer_license = LI.license_code
            '''.format(query = sorguCumlesi))
    else:
        rows2 = ""

    return render(request, 'search.html', {'rows': rows, 'rows2': rows2, 'keywords': keywords, 'rowstotal': rowstotal, 'oneriListesi': oneriListesi})

def test_view(request):

    return render(request, 'test.html')