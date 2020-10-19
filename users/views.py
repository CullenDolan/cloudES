from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

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

'''
message methods:
messages.debug
messages.info
messages.success
messages.warning
messages.error
'''