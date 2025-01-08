"""Model for portfolio Owner's activities' images."""

from django.db import models

from myapp.models import Activity


class ActivityImage(models.Model):
    """
    Represents images of illustrations that is part of the Owner's portfolio.
    """
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f'{self.activity} photo'
