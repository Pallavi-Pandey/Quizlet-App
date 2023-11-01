from django.shortcuts import render, redirect
from .forms import FlashcardForm, UserRegistrationForm, UserLoginForm, DeckForm
from .models import Deck, Flashcard
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

@login_required
def create_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect('home')
    else:
        form = DeckForm()
    return render(request, 'create_deck.html', {'form': form})

@login_required
def view_deck(request, deck_id):
    deck = Deck.objects.get(id=deck_id)
    flashcards = Flashcard.objects.filter(deck=deck)
    return render(request, 'view_deck.html', {'deck': deck, 'flashcards': flashcards})

@login_required
def add_flashcard(request, deck_id):
    deck = Deck.objects.get(id=deck_id)
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.deck = deck
            flashcard.save()
            return redirect('view_deck', deck_id=deck.id)
    else:
        form = FlashcardForm()
    return render(request, 'add_flashcard.html', {'form': form, 'deck': deck})

@login_required
def home(request):
    user_decks = Deck.objects.filter(user=request.user)
    return render(request, 'home.html', {'user_decks': user_decks})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or perform other actions
                return render(request, 'home.html')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')