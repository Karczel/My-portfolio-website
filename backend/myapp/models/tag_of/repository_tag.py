"""Model representing the tags the Owner of portfolio's activity may have."""

from django.db import models

from myapp.models import Repository, Tag


class RepositoryTag(models.Model):
    """
    Represents tags of activity that is part of the Owner's portfolio.
    """
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.repository}, {self.tag}'
