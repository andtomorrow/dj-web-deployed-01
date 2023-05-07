from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from django.conf import settings


class BrewLog(models.Model):

    class Location(models.TextChoices):
        HOME = 'HOM', _('집, Home Sweet Home')
        CAFE = 'CAF', _('카페, 커피숍')
        TEAROOM = 'TEA', _('티룸, 찻집')
        OUTDOOR = 'OUT', _('야외, 캠핑')
        ETC = 'ETC', _('그 외의 장소')

    class Satisfaction(models.IntegerChoices):
        NOT_BAD = 1
        NICE = 2
        FAVORITE = 3
        PURE_JOY = 4
        HAPPINESS = 5

    author = models.ManyToManyField(settings.AUTH_USER_MODEL)
    recipe = models.ManyToManyField("recipes.Recipe", verbose_name=_("recipe chosen"))
    when = models.DateTimeField(_("time and date"),default=timezone.now)
    num_hearts = models.IntegerField(_("Number of hearts"), choices=Satisfaction.choices)
    where = models.CharField(choices=Location.choices, verbose_name=_("place"), max_length=3)