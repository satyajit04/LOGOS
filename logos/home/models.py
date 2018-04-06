from django.db import models
from django.contrib.auth.models import Permission, User
from multiselectfield import MultiSelectField

# Create your models here.

class Paduka(models.Model):

    COLORS = (
        ('Jute Color', 'Jute Color'),
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Yellow', 'Yellow'),
        ('White', 'White'),
        ('Black', 'Black'),
        ('Purple', 'Purple'),
        ('Maroon', 'Maroon'),
        ('Orange', 'Orange'),
        ('Black & White', 'Black & White'),
        ('Olive Green', 'Olive Green'),
        ('Navy blue', 'Navy Blue'),
        ('Dark Grey', 'Dark Grey'),
        ('Stripe', 'Stripe'),
    )

    DIVISIONS = (
        ('Sandal', 'Sandal'),
        ('Slipper', 'Slipper'),
        ('Espadrille', 'Espadrille'),
    )

    prototype_id = models.CharField('Number', max_length=10)
    image = models.FileField(null=True, blank=True)
    season = models.CharField(max_length=20)
    division = models.CharField(max_length=50, choices=DIVISIONS)
    color_description = MultiSelectField(choices=COLORS)
    price = models.FloatField(null=True)
    upper = models.CharField(max_length=100)
    footbed = models.CharField(max_length=100)
    footbed_skin = models.CharField(max_length=100)
    edge_treatment_upper = models.CharField(max_length=100)
    edge_color = models.CharField(max_length=100)
    edge_treatment_sole = models.CharField(max_length=100)
    logo = models.CharField(max_length=50)
    heel = models.CharField(max_length=50)

    def __str__(self):
        return self.prototype_id + '-' + self.division

