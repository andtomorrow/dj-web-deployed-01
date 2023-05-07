from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserCreate(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'favorite_beverage', 'favorite_place',]


class UserChange(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'favorite_beverage', 'favorite_place',]