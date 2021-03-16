from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def registerUser(request):
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account wurde erfolgreich erstellt.")
            return redirect("login")
        else:
            messages.error(request, "fuck")
            return redirect("registerUser")

    else:

        form = UserCreationForm()
        return render(request, "users/registerUser.html", {"form": form})

