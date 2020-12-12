from django.contrib import admin

from .models import oersTest

class oersTestAdmin(admin.ModelAdmin):
    #Liste görünümünde
    list_display = ('id','oer_name','oer_url')
    #Kaydın içine girince
    #fields = ['oer_name','oer_url']
    #Formu Bölümlere Ayırmak
    fieldsets = [
        ('Ad Bölümü', {'fields': ['oer_name']}),
        ('URL Bölümü', {'fields': ['oer_url']}),
    ]

admin.site.register(oersTest, oersTestAdmin)