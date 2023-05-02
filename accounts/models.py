from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_PLACE = (
        ('Home', '집'),
        ('Cafe', '커피숍'),
        ('TeaBoutique', '티룸'),
        ('Outdoor', '실외'),
        ('Other', '기타'),
    )
    favorite_bev = models.CharField(max_length=30)
    home_base = models.CharField(blank=True, choices=USER_PLACE, max_length=30)
