from django.contrib.auth.admin import User
from .models import tweettable, favtable
from django import forms


class register_form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username','password','email']

class twitter_form(forms.ModelForm):

    class Meta:

        model = tweettable
        fields = ['tweet']

class edit_form(forms.ModelForm):

    class Meta:

        model = tweettable
        fields = ['tweet']