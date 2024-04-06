from django import forms

class MyForm(forms.Form):
    message = forms.CharField(label='Your Prompt', widget=forms.Textarea)

class LoginForm(forms.Form):
    UserName = forms.CharField(label='User Name', widget=forms.Textarea)
    Password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

from django import forms

class CreateAccountForm(forms.Form):
    UserName = forms.CharField(label='User Name', max_length=100)
    Password = forms.CharField(label='Password', widget=forms.PasswordInput())
    ReenterPassword = forms.CharField(label='Re-enter Password', widget=forms.PasswordInput())
