from django.contrib import admin

# Register your models here.
from .models import OerData
from .models import TypeData

class OerDataAdmin(admin.ModelAdmin):
    #Liste görünümünde
    list_display = ('oer_auto_id','oer_auto_date','oer_title','oer_identifier')
    list_filter = ('oer_title','oer_license',)
    # Form Bölümleri
    fieldsets = [
        ('İçerik', {'fields': ['oer_title','oer_subject','oer_description','oer_type']}),
        ('Entellektüel', {'fields': ['oer_creator','oer_publisher','oer_contributor','oer_license']}),
        ('Yapısal', {'fields': ['oer_date','oer_language','oer_format','oer_identifier']}),
        ('Eğitsel', {'fields': ['oer_educationalAudience','oer_educationalUse','oer_accessibilityFeature','oer_timeRequired']})
    ]
    search_fields = ('oer_title','oer_subject','oer_description','oer_type')

class TypeDataAdmin(admin.ModelAdmin):
    #Liste görünümünde
    list_display = ('type_auto_id','type_auto_date','type_name')

admin.site.register(OerData, OerDataAdmin)
admin.site.register(TypeData, TypeDataAdmin)