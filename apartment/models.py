from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Appartments(models.Model):
    title = models.CharField(max_length = 200)
    price = models.PositiveIntegerField()
    slug = models.SlugField(max_length = 200, default = "irabi")
    # image = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    # def slug(self):
    #     return slugify(self.title)
    class Meta:
        verbose_name_plural = "Appartments"
    def __str__(self):
        return self.title
