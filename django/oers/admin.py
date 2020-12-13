from django.contrib import admin

from .models import oersTest
from .models import oer_data

class oersTestAdmin(admin.ModelAdmin):
    #Liste görünümünde
    list_display = ('id','oer_name','oer_url')
    #Kaydın içine girince
    #fields = ['oer_name','oer_url']
    #Formu Bölümlere Ayırmak
    fieldsets = [
        ('Ad Bölümü', {'fields': ['oer_name']}),
        ('URL Bölümü', {'fields': ['oer_url','oer_types']}),
    ]

class oer_dataAdmin(admin.ModelAdmin):
    #Liste görünümünde
    list_display = ('oer_auto_id','oer_auto_date','oer_title','oer_identifier')
    list_filter = ('oer_title','oer_license',)
    # Form Bölümleri
    fieldsets = [
        ('İçerik', {'fields': ['oer_title','oer_subject','oer_description','oer_type']}),
        ('Entellektüel', {'fields': ['oer_creator','oer_publisher','oer_contributer','oer_license']}),
        ('Yapısal', {'fields': ['oer_date','oer_language','oer_format','oer_identifier']}),
        ('Eğitsel', {'fields': ['oer_educationalAudience','oer_educationalUse','oer_accesibilityFeature','oer_timeRequired']})
    ]
    search_fields = ('oer_title','oer_subject','oer_description','oer_type')

admin.site.register(oersTest, oersTestAdmin)
admin.site.register(oer_data, oer_dataAdmin)