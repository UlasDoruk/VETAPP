from re import search
from django.contrib import admin
from . models import Owners

# Django admin site calls Owners model 

@admin.register(Owners)

# Django Admin side display properties

class OwnersAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available',)
    search_fields = ('name',)


# admin username : ulasdk
# password : 7272

