from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CommentForms(forms.ModelForm):
    class Meta:
        model =  Comment
        fields = ['text','image']
        
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        
        model = User
        fields = ('username','email','password1','password2')        
              