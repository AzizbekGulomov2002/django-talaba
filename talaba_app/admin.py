from django.contrib import admin

# Register your models here.

from .models import Talaba


class TalabaAdmin(admin.ModelAdmin):
    list_display = ['ism', 'familiya', 'tug_yil', 'tel', 'jins']
    
    
admin.site.register(Talaba, TalabaAdmin)