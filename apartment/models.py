from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Appartments(models.Model):
    kitchen_room = (
        ('True','True'),('False','False')
    )
    roomtype = (
        ('Furnished','Furnished'),('Unfurnished','Unfurnished')
    )
    title = models.CharField(max_length = 200)
    price = models.PositiveIntegerField()
    slug = models.SlugField(max_length = 200, default = "irabi")
    area_range = models.PositiveIntegerField(default = 1200)
    room_type = models.CharField(max_length = 50, default = "Furnished", choices = roomtype)
    Bedrooms = models.PositiveIntegerField(default = 2)
    Bathroom = models.PositiveIntegerField(default = 2)
    kitchen = models.CharField(max_length = 10, default = "True", choices = kitchen_room)
    image = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')

    # def slug(self):
    #     return slugify(self.title)
    class Meta:
        verbose_name_plural = "Appartments"
    def __str__(self):
        return self.title
