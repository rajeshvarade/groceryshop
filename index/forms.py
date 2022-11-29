from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','Placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'form-control','Placeholder':'Password'}))


class SignUpForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','Placeholder':'Username',}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs = {'class':'form-control','Placeholder':'Password'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs = {'class':'form-control','Placeholder':'Confirm Password'}))
    