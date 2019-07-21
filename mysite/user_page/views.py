from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import Userform, LoginForm, NewGame
from django.http import HttpResponseRedirect
from .repository import UserGames, Games


def user(request):
    if request.user.is_authenticated:
        user = request.user
        usergames = UserGames()
        existinggames = Games.getgamesandratings(user.id)
        print(existinggames)
        if request.POST.get('action') == 'Game':
            gameform = NewGame(request.POST)
            if gameform.is_valid():
                game = gameform.cleaned_data['game']
                newrating = gameform.cleaned_data['rating']
                newgameid = Games.getid(game)
                if game is not None:
                    if existinggames == []:
                        usergames.newgame(user.id, newgameid)
                        usergamesid = usergames.getusergamesid(user.id, newgameid)
                        usergames.newrating(usergamesid, newrating)
                    elif game not in existinggames[0].values():
                        usergames.newgame(user.id, newgameid)
                        usergamesid = usergames.getusergamesid(user.id, newgameid)
                        usergames.newrating(usergamesid, newrating)
                return HttpResponseRedirect('')

        else:
            gameform = NewGame()
        return render(request, 'user.html', {'title':'User Page',
                                             'user':user,
                                             'games':existinggames,
                                             'gameform':gameform,
                                             'test': '1'})
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(request,username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                return HttpResponseRedirect('/user/')
        else:
            form = LoginForm()

    return render(request, 'login.html', {'form': form, 'title':'Login'})


def createuser(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'],
                                            email=form.cleaned_data['email'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'])
            user.save()
            print(user.save())
            print(form.cleaned_data)
            return HttpResponseRedirect('/user/')
    else:
        form = Userform()

    return render(request, 'createuser.html', {'form': form, 'title': 'Create Account'})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/user/')





