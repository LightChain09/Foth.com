from django.shortcuts import render, redirect
from .models import Suggestions
from .forms import CreateSuggestion


def show_suggestions(request):

    suggestions = Suggestions.objects.all()

    return render(request, 'suggestions/show_suggestions.html', {"suggestions": suggestions})


def create_suggestion(request):

    if request.method == "POST":
        form = CreateSuggestion(request.POST)

        if form.is_valid():
            cleaned_data = form.clean()
            form.save()

            return redirect("show_suggestions")


    form = CreateSuggestion()

    return render(request, 'suggestions/create_suggestion.html', {"form": form})