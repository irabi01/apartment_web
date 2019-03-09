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


class Booking(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email_address = models.CharField(max_length = 100)
    phone_number = models.PositiveIntegerField()
    check_in = models.CharField(max_length = 25)
    check_out = models.CharField(max_length = 25)
    class Meta:
        verbose_name_plural = "Booking Details"
    def __str__(self):
        return self.first_name + " " + self.last_name + "-" + self.email_address