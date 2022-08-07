from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from account.forms import UserForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            id, pw = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
            user = authenticate(username=id, password=pw)
            login(request, user)
            return redirect('board:index')
    else: form = UserForm()
    return render(request, 'account/signup.html', {'form': form})
            
