"""Model for portfolio Owner's repositories' images."""

from django.db import models

from myapp.models import Repository


class RepositoryImage(models.Model):
    """
    Represents images of illustrations that is part of the Owner's portfolio.
    """
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f'{self.repository} photo'
