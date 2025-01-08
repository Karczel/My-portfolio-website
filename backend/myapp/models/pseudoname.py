"""Model for portfolio Owner's pseudo names."""

from django.db import models

from myapp.utils import NAME


class PseudoName(models.Model):
    """
    Represents pseudo names of owner of portfolio.
    """
    name = models.CharField(max_length=NAME)

    def __str__(self):
        return self.name
