from django.db import models
from django.utils.translation import gettext_lazy as _


class Beverage(models.Model):
    bev_name = models.CharField(_("beverage name"), max_length=50)
    

class Recipe(models.Model):

    class TemperatureType(models.TextChoices):
        ROOM = 'ROOM', _('상온')
        HOT = 'HOT', _('뜨겁게')
        WARM = 'WARM', _('따뜻하게')
        COOL = 'COOL', _('시원하게')
        ICED = 'ICED', _('얼음 넣어서')
    
    beverage = models.ForeignKey("Beverage", on_delete=models.CASCADE)
    temp_type = models.CharField(max_length=10, choices=TemperatureType.choices, default=TemperatureType.WARM)
    brew_details = models.TextField(_("Brew details"), blank=True)

