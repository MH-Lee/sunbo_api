from django.contrib import admin
from .models import (
    CompanyCode, EM01,
    AA06, AA22, AB01,
    AB09, AD01, AZ06
    )

# Register your models here.
class CompanyCodeAdmin(admin.ModelAdmin):
    list_display = ('com_code', 'com_name')

class EM01Admin(admin.ModelAdmin):
    list_display = ('com_code', 'com_abbreviation')

class AA06Admin(admin.ModelAdmin):
    list_display = ('date', 'com_code')

class AA22Admin(admin.ModelAdmin):
    list_display = ('date', 'com_code')

class AB01Admin(admin.ModelAdmin):
    list_display = ('date', 'com_code')

class AB09Admin(admin.ModelAdmin):
    list_display = ('rep_code', 'item_code', 'item_name')

class AD01Admin(admin.ModelAdmin):
    list_display = ('date', 'com_code')

class AZ06Admin(admin.ModelAdmin):
    list_display = ('date', 'com_code')

admin.site.register(CompanyCode, CompanyCodeAdmin)
admin.site.register(EM01, EM01Admin)
admin.site.register(AA06, AA06Admin)
admin.site.register(AA22, AA22Admin)
admin.site.register(AB01, AB01Admin)
admin.site.register(AB09, AB09Admin)
admin.site.register(AD01, AD01Admin)
admin.site.register(AZ06, AZ06Admin)
