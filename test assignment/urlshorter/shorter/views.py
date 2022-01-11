from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import  UserRegistration, UserLogIn, AddUrl
from .models import Url

# Create your views here.

def register(request):

    if request.method == 'POST':
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return HttpResponse('<h1>Register succes</h1>')
    else:
        user_form = UserRegistration()

    return render(request, 'register.html', {'user_form': user_form})

def loginUser(request):

    if request.method == 'POST':
        form = UserLogIn(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)

                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = UserLogIn()

    return render(request, 'login.html', {'form': form})


def logoutUser(request):

    if request.user.is_authenticated:
        logout(request)

        return render(request, 'logged_out.html')
    else:
        return HttpResponse('<h1>You didn\'t login</h1>')

def shorter(request):

    form = AddUrl(request.POST or None)
    if request.method == 'POST':
        long_url = request.POST.get('long_url')

        if Url.objects.filter(long_url=long_url, user_id=request.user.id).exists():
            obj = Url.objects.get(long_url=long_url, user_id=request.user.id)

            return render(request, 'shorter.html', {
                        'short_url': request.get_host() + '/' + obj.short_url[-6:],
                        'form': form
                        })
        else:
            if request.user.is_authenticated:
                obj = Url.create(long_url, request.user)

                return render(request, 'shorter.html', {
                            'short_url': request.get_host() + '/' + obj.short_url[-6:],
                            'form': form
                            })
            else:
                return HttpResponse('<h1>You didn\'t login</h1>')

    return render(request, 'shorter.html',{'form': form})

def routeTo(request, key):
    
    try:
        obj = Url.objects.get(short_url=request.get_host() + '/' + key, user_id=request.user.id)
        return redirect(obj.long_url)
    except BaseException:
        return redirect(shorter)

def showLinks(request):
    arrayLinks = []

    if request.method == 'POST':
        if request.user.is_authenticated:
            for obj in Url.objects.filter(user_id=request.user):
                arrayLinks.append(obj.short_url)

            return render(request, 'showlinks.html',{
                        'short_urls': arrayLinks
                        })
        else:
            return HttpResponse('<h1>Please login</h1>')

    return render(request, 'showlinks.html')