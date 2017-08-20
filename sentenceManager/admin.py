from django.contrib import admin
from .models import Sentence

class SentenceAdmin(admin.ModelAdmin):
    list_display = ("audioFile", "sentence", "hasError", "getAllWords")

    def getAllWords(self, obj):
        return "\n".join([w.word for w in obj.words.all()])

admin.site.register(Sentence, SentenceAdmin)