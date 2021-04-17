from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm



def registerUser(request):
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account wurde erfolgreich erstellt.")
            return redirect("login")
        else:
            messages.error(request, "Ein Fehler ist aufgetreten...")
            return redirect("registerUser")

    else:

        form = UserCreationForm()
        return render(request, "users/registerUser.html", {"form": form})

    
@login_required
def userProfile(request):

    if request.method == "POST":

        profileUpdateForm = ProfileUpdateForm(request.POST)

        if profileUpdateForm.is_valid():
            profileUpdateForm.save()
            messages.success(request, "Steam ID wurde erfolgreich aktualisiert.")
        else:
            messages.error(request, "Ein Fehler ist aufgetreten.")
        
        return redirect("userProfile")

    else:

        profileUpdateForm = ProfileUpdateForm()

        return render(request, "users/userProfile.html", {"profileUpdateForm": profileUpdateForm})
