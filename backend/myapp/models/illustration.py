"""Model for portfolio Owner's illustrations."""

from django.db import models


class Illustration(models.Model):
    """
    Represents illustrations that is part of the Owner's portfolio.
    """
    image = models.ImageField()
    name = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.image
