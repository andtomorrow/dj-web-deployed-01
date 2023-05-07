from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class FavoritePlace(models.TextChoices):
        HOME = 'HOM', _('집, Home Sweet Home')
        CAFE = 'CAF', _('카페, 커피숍')
        TEAROOM = 'TEA', _('티룸, 찻집')
        OUTDOOR = 'OUT', _('야외, 캠핑')
        ETC = 'ETC', _('그 외의 장소')

    favorite_place = models.CharField(max_length=3, choices=FavoritePlace.choices, default=FavoritePlace.HOME)
    
    favorite_beverage = models.ForeignKey("recipes.Beverage", on_delete=models.CASCADE)