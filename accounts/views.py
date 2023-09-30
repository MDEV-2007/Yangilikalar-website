from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user = authenticate(request, 
            username = data['username'],
            password = data['password']
            )
            if user is not None:
                if user.is_active():
                    login(request, user)
                    return HttpResponse("Muvaffaqiytli login")
                else:
                    return HttpResponse("Sining accountningiz faol holatda emas")
            else:
                return HttpResponse("Parol yoki username xato")
    else:
        form = LoginForm()
        context = {
            "form": form,
        }
    return render(request, 'accounts/login.html',context)