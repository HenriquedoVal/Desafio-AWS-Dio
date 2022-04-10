from django.contrib import admin
from core.models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'episodes', 'curr_ep', 'last_view')

admin.site.register(Movie, MovieAdmin)
