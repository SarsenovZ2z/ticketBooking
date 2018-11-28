from django.contrib import admin
from .models import Country, City

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'code')


class CityAdmin(admin.ModelAdmin):
    search_fields = ['country__name']
    list_display = ('name', 'short_name', 'country')

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
