from django import forms
from django.contrib.auth.models import User 
from traveleverywhere.models import User_Profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta: 
        model = User 
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm): 
    class Meta: 
        model = User_Profile 
        fields = ('about', 'picture',)

