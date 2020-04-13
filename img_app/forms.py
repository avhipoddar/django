from django import forms
from .models import User,UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    
    class Meta:
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):

    

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_url','profile_pic')

        

