from django import forms

class LoginForm(forms.Form):

    username = forms.CharField()
    pwd = forms.CharField()