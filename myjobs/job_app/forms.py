from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from . import models

class UserRegistrationForm(UserCreationForm):
        class Meta:
                model=User
                fields = ['username','email']          
                labels = {
                        'email':'Email',
                        'password2':'Confirm Password'
                }

class UserProfileForm(forms.ModelForm):
        class Meta:
                model = models.UserProfileModel
                fields = '__all__'


class JobForm(forms.ModelForm):
        # expire_on = forms.DateField()
        class Meta:
                model = models.JobModel
                fields = '__all__'


class ApplyJobForm(forms.ModelForm):
        class Meta:
                model = models.ApplyJobModel
                fields = '__all__'