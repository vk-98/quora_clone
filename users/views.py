from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def register(request):

    if request.method == 'POST':
        form  = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Registered successfully')
            return redirect('home')

    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)



def DisplayProfile(request, uname):

    userProfile = get_object_or_404(User, username = uname)
    print(userProfile.email)
    return render(request, 'users/profile.html', {'userProfile': userProfile})