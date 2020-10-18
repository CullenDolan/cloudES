from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# so users can sign up for a site
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('blog-home') # redirects to url pattern
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

'''
message methods:
messages.debug
messages.info
messages.success
messages.warning
messages.error
'''