from django import forms
from .repository import Games

class Userform(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class NewGame(forms.Form):
    game = forms.ChoiceField(choices=[(x['name'], x['name']) for x in Games.allgames()])
    rating = forms.FloatField(label='Rating', max_value=100, min_value=0)
