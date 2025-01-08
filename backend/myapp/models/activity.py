"""Model for portfolio Owner's activities."""

from django.db import models

from myapp.utils import NAME, ROLE


class Activity(models.Model):
    """
    Represents Activity the Owner of the portfolio has participated.
    """
    name = models.CharField(max_length=NAME)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=ROLE, default="member")

    def __str__(self):
        return self.name
