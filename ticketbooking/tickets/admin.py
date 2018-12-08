from django.contrib import admin
import nested_admin

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

class SessionInline(nested_admin.NestedStackedInline):
    model = Session
    list_display = ('id', 'film', 'hall', 'price', 'start_at', 'end_at')
    extra = 0


class HallInline(nested_admin.NestedStackedInline):
    model = Hall;
    extra = 0
    list_display = ('name', 'cinema', 'rows', 'seats')
    inlines = [
        SessionInline
    ]

class CinemaAdmin(nested_admin.NestedModelAdmin):
    list_display = ('name', 'city', 'description', 'website', 'lat', 'lon')
    inlines = [
        HallInline,
    ]

class PosterInline(admin.TabularInline):
    model = Poster
    list_display = ('title', 'image')
    extra = 0

class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'premiere', 'description', 'main_poster')
    inlines = [
        PosterInline
    ]

class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'hall', 'price', 'start_at', 'end_at')

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'created_at', 'row', 'col')

class PosterAdmin(admin.ModelAdmin):
    list_display = ('image', 'film', 'title')

admin.site.register(Country, CountryAdmin)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Poster, PosterAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Ticket, TicketAdmin)
