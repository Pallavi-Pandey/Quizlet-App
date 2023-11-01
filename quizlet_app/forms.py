from django import forms
from .models import Deck, Flashcard
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['title']

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['question', 'answer']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
