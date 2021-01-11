from django.db import models

# Create your models here.
class OerData(models.Model):
    oer_auto_id = models.AutoField(verbose_name="OER ID", primary_key=True)
    oer_auto_date = models.DateTimeField(verbose_name="Kayıt Tarihi ve Saati", auto_now=True)
    oer_title = models.CharField(verbose_name="Başlık", max_length=500)
    oer_subject = models.CharField(verbose_name="Konu", max_length=1000)
    oer_description = models.TextField(verbose_name="Özet")
    oer_type = models.CharField(verbose_name="Kaynak Tipi", max_length=500)
    oer_creator = models.CharField(verbose_name="Yaratıcı", max_length=500)
    oer_publisher = models.CharField(verbose_name="Yayıncı", max_length=500, null=True, blank=True)
    oer_contributor = models.CharField(verbose_name="Katkı Sağlayan", max_length=500, null=True, blank=True)
    oer_license = models.CharField(verbose_name="Açık Lisans", max_length=100)
    oer_date = models.DateField(verbose_name="Tarih", null=True, blank=True)
    oer_language = models.CharField(verbose_name="Dil", max_length=100, null=True, blank=True)
    oer_format = models.CharField(verbose_name="Dosya Biçimi", max_length=100, null=True, blank=True)
    oer_identifier = models.CharField(verbose_name="Tanımlayıcı Adres (URL)", max_length=500)
    oer_educationalAudience = models.CharField(verbose_name="Hedef Kitle", max_length=500, null=True, blank=True)
    oer_educationalUse = models.CharField(verbose_name="Eğitsel Kullanım", max_length=500, null=True, blank=True)
    oer_accessibilityFeature = models.CharField(verbose_name="Erişilebilirlik Özellikleri", max_length=100, null=True, blank=True)
    oer_timeRequired = models.IntegerField(verbose_name="İhtiyaç Duyulan Süre", null=True, blank=True)

class TypeData(models.Model):
    type_auto_id = models.AutoField(verbose_name="OER ID", primary_key=True)
    type_auto_date = models.DateTimeField(verbose_name="Kayıt Tarihi ve Saati", auto_now=True)
    type_name = models.CharField(verbose_name="Ad", max_length=50)

class LicenseData(models.Model):
    license_auto_id = models.AutoField(verbose_name="License ID", primary_key=True)
    license_auto_date = models.DateTimeField(verbose_name="Kayıt Tarihi ve Saati", auto_now=True)
    license_code = models.CharField(verbose_name="Code", max_length=50)
    license_icon = models.CharField(verbose_name="Icon", max_length=1000)
    license_deed = models.CharField(verbose_name="URL", max_length=500)
    license_info = models.CharField(verbose_name="Info", max_length=500)