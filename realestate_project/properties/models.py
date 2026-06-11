from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):

    PROPERTY_TYPES = (
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    )

    title = models.CharField(max_length=200)

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    address = models.CharField(
        max_length=255
    )

    image = models.ImageField(
        upload_to='properties/'
    )

    property_type = models.CharField(
        max_length=10,
        choices=PROPERTY_TYPES
    )
     owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
