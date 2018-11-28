from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Cinema, Hall


class HallInline(NestedStackedInline):
    model = Hall
    fk_name = 'cinema'
    extra = 0
    list_display = ('cinema', 'name', 'seats')

class CinemaAdmin(NestedModelAdmin):
    list_display = ('name', 'city', 'website', 'rating', 'votes', 'content', 'lat', 'lon')
    inlines = [HallInline]


admin.site.register(Cinema, CinemaAdmin)
