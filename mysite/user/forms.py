from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.forms import TextInput, EmailInput, PasswordInput, CharField, EmailField, DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ToDo


class UserRegistrationForm(UserCreationForm):
    # email = CharField(widget=EmailInput(attrs={'class': 'form-control'}))
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        # username = CharField(widget=TextInput(attrs={'class': 'form-control', }))
        # first_name = CharField(widget=TextInput(attrs={'class': 'form-control', }))
        # last_name = CharField(widget=TextInput(attrs={'class': 'form-control', }))

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'id': '1'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
            }),
            # 'password1': PasswordInput(attrs={
            #     'class': 'form-control',
            # }),
            # 'password2': PasswordInput(attrs={
            #     'class': 'form-control',
            # })
        }


class UserLoginForm(forms.Form):
    username = CharField(widget=TextInput(attrs={'class': 'form-control', }))
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control'}))


class ToDoForm(forms.ModelForm):
    name = CharField(widget=TextInput(attrs={'class': 'form-control', 'type': "text"}))
    end_date = forms.DateField(widget=DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = ToDo
        fields = ['name', 'status', 'end_date']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'type': "text",
            }),
        }
