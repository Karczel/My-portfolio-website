"""Model for portfolio Owner's videos."""

from django.db import models

from myapp.utils import NAME


class Video(models.Model):
    """
    Represents video that is part of the Owner's portfolio.
    """
    name = models.CharField(max_length=NAME)
    desc = models.TextField(blank=True, null=True)
    link = models.TextField()

    def __str__(self):
        return self.name
