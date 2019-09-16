from django.contrib import admin
from .models import (
    em01, aa22, aa06,
    ab01, ab09, ad01,
    az06
    )

# Register your models here.
class em01Admin(admin.ModelAdmin):
    list_display = ('com_code', 'com_name_ko')

class aa06Admin(admin.ModelAdmin):
    list_display = ('date', 'com_code')

class aa22Admin(admin.ModelAdmin):
    list_display = ('date', 'com_code')

class ab01Admin(admin.ModelAdmin):
    list_display = ('date', 'com_code')

class ab09Admin(admin.ModelAdmin):
    list_display = ('rep_key',)

class ad01Admin(admin.ModelAdmin):
    list_display = ('date', 'com_code')

class az06Admin(admin.ModelAdmin):
    list_display = ('date', 'com_code')

admin.site.register(em01, em01Admin)
admin.site.register(aa06, aa06Admin)
admin.site.register(aa22, aa22Admin)
admin.site.register(ab01, ab01Admin)
admin.site.register(ab09, ab09Admin)
admin.site.register(ad01, ad01Admin)
admin.site.register(az06, az06Admin)
