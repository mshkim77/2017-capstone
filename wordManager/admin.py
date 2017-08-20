from django.contrib import admin
from .models import Word

class WordAdmin(admin.ModelAdmin):
    list_display = ("word", "rage", "loathing", "grief", "amazement", "terror", "admiration", "ecstasy", "vigilance")

admin.site.register(Word, WordAdmin)