from django.db import models

TYPES = [
    ('Etkileşimli Kaynak','Etkileşimli Kaynak'),
    ('Etkinlik','Etkinlik'),
    ('Fiziksel Nesne','Fiziksel Nesne'),
    ('Görsel','Görsel'),
    ('Hareketli Görsel','Hareketli Görsel'),
    ('Hareketsiz Görsel','Hareketsiz Görsel'),
    ('Koleksiyon','Koleksiyon'),
    ('Metin','Metin'),
    ('Servis','Servis'),
    ('Ses','Ses'),
    ('Veri seti','Veri seti'),
    ('Yazılım','Yazılım'),
]

class oersTest(models.Model):
    oer_name = models.CharField(max_length=200)
    oer_url = models.CharField(max_length=200)
    oer_types = models.CharField(max_length=100, choices=TYPES)

class oer_data(models.Model):
    oer_auto_id = models.AutoField(primary_key=True)
    oer_auto_date = models.DateTimeField(verbose_name="Kayıt Tarihi ve Saati", auto_now=True)
    oer_title = models.CharField(verbose_name="Başlık",max_length=500)
    oer_subject = models.CharField(verbose_name="Konu", max_length=1000)
    oer_description = models.TextField(verbose_name="Özet")
    oer_type = models.CharField(verbose_name="Kaynak Tipi", max_length=500)
    oer_creator = models.CharField(verbose_name="Yaratıcı", max_length=500)
    oer_publisher = models.CharField(verbose_name="Yayıncı", max_length=500, null=True, blank=True)
    oer_contributer = models.CharField(verbose_name="Katkı Sağlayan", max_length=500, null=True, blank=True)
    oer_license = models.CharField(verbose_name="Açık Lisans", max_length=100)
    oer_date = models.DateField(verbose_name="Tarih", null=True, blank=True)
    oer_language = models.CharField(verbose_name="Dil", max_length=100, null=True, blank=True)
    oer_format = models.CharField(verbose_name="Dosya Biçimi", max_length=100, null=True, blank=True)
    oer_identifier = models.CharField(verbose_name="Tanımlayıcı Adres (URL)", max_length=500)
    oer_educationalAudience = models.CharField(verbose_name="Hedef Kitle", max_length=500, null=True, blank=True)
    oer_educationalUse = models.CharField(verbose_name="Eğitsel Kullanım", max_length=500, null=True, blank=True)
    oer_accesibilityFeature = models.CharField(verbose_name="Erişilebilirlik Özellikleri", max_length=100, null=True, blank=True)
    oer_timeRequired = models.IntegerField(verbose_name="İhtiyaç Duyulan Süre", null=True, blank=True)

class OerTypeValues(models.Model):
    oer_type_id = models.AutoField(primary_key=True)
    oer_type_name = models.CharField(verbose_name="Başlık",max_length=100)

"""
class OerLicenceValue(models.Model):
    oer_licence_id = models.AutoField(primary_key=True)
    oer_licence_name = models.CharField(verbose_name="Lisans Adı",max_length=100)
    oer_license_deed = models.CharField(verbose_name="Lisans URL",max_length=500)
    oer_license_html = models.CharField(verbose_name="Lisans URL",max_length=1000)
"""