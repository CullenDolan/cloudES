from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# so users can sign up for a site
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # saves user and keeps it secure
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created an you can login {username}')
            return redirect('login') # redirects to url pattern

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required  # a decorator adds functionality to a function
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile') # redirects to url pattern
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)  
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

'''
message methods:
messages.debug
messages.info
messages.success
messages.warning
messages.error
'''