from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from accounts.models import Avatar


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class UpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("IMG",)