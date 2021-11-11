from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput
from allauth.account.forms import LoginForm


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class MyCustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["login"].label = ""
        self.fields["password"].label = ""
        # self.remember = None
        # self.fields['remember'].lab = None

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        self.fields["login"].label = ""
        self.fields["password"].label = ""
        # self.remember = None
        return super(MyCustomLoginForm, self).login(*args, **kwargs)

# class CustomAuthForm(AuthenticationForm):
#     email = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Email'}))
#     password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))