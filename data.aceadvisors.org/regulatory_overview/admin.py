from django.contrib import admin
from django import forms
from .models import *


class RegulatoryAdmin(admin.ModelAdmin):
    list_display = ('PdfTitle', 'created')
    list_filter = ('updated', )
    search_fields = ('PdfTitle',)
    list_per_page = 10
class StrategyAdmin(admin.ModelAdmin):
    list_display = ('PdfTitle', 'created')
    list_filter = ('updated', )
    search_fields = ('PdfTitle',)
    list_per_page = 10
class OtherAdmin(admin.ModelAdmin):
    list_display = ('PdfTitle', 'created')
    list_filter = ('updated', )
    search_fields = ('PdfTitle',)
    list_per_page = 10

admin.site.register(NationalStrategies, StrategyAdmin)
admin.site.register(BusinessStrategy, RegulatoryAdmin)
admin.site.register(OtherStudie, OtherAdmin)
admin.site.register(ImportantLinks)
admin.site.register(DataRepository)
admin.site.register(Region)
admin.site.register(Year)
#admin.site.register(EndYear)
