from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import HiddenInput
from django.forms.widgets import Select

from .models import Employee, HourTableStart, HourTableEnd
import datetime


class EmpForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class StartTime(ModelForm):
    class Meta:
        model = HourTableStart
        fields = ['building']



class EndTime(ModelForm):
    class Meta:
        model = HourTableEnd
        fields = ['building']


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


"""
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('custom_field',)"""
