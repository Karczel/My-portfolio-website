"""Model for portfolio Owner's contacts."""

from django.db import models

from myapp.utils import NAME


class Contact(models.Model):
    """
    Represent contacts of Owner of the portfolio.
    """
    platform = models.CharField(max_length=NAME)
    icon = models.ImageField()
    link = models.TextField()

    def __str__(self):
        return self.platform
