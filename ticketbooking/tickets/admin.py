from django.contrib import admin

from .models import *
# Register your models here.

class CityInline(admin.TabularInline):
    model = City;
    extra = 0
    list_display = ('id', 'country', 'short_name', 'name')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'short_name', 'name')
    inlines = [
        CityInline,
    ]

class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'description', 'website', 'lat', 'lon')


admin.site.register(Country, CountryAdmin)
admin.site.register(Cinema, CinemaAdmin)
