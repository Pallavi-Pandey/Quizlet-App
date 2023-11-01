from django.contrib import admin
from .models import Deck, Flashcard, UserProfile

# Register your models here.

admin.site.register(Deck)
admin.site.register(Flashcard)
admin.site.register(UserProfile)

