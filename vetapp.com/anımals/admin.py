from re import search
from django.contrib import admin
from . models import Anımals

@admin.register(Anımals)

class AnımalsAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available',)
    search_fields = ('name',)




# admin username : udk97@hotmail.com
# password : 7272
