from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def logout_view(request):
    """log the user out"""
    logout(request)
    return redirect('learning_logs:index')


def register(request):
    """register a new user"""
    if request.method != "POST":
        """display a blank registration form"""
        form = UserCreationForm()
    else:
        # process completed form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
        # log the user in then redirect to home page
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'users/register.html', context)
