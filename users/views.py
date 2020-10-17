from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# so users can sign up for a site
def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
