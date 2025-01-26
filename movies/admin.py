from django.contrib import admin
from .models import Movie
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','director','genre','release_date')
    search_fields = ('genre','director','release_date')
    ordering  = ('genre','title')
    