from django.shortcuts import render, redirect
from.models import User
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # saves the user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)  # instances are there so that it knows what user and profile to update
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)  # Part 9, so is the line above
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)  # Part 9 (Args so that the info is already filled in)
        p_form = ProfileUpdateForm(instance=request.user.profile)  # Part 9 (Args so that the info is already filled in)

    context = {
        'u_form': u_form,  # Part 9
        'p_form': p_form  # Part 9
    }

    return render(request, 'users/profile.html', context)
