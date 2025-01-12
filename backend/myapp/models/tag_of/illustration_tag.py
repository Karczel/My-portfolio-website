"""Model representing the tags the Owner of portfolio's activity may have."""

from django.db import models

from myapp.models import Illustration, Tag


class IllustrationTag(models.Model):
    """
    Represents tags of illustrations that is part of the Owner's portfolio.
    """
    illustration = models.ForeignKey(Illustration, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
            constraints = [
                models.UniqueConstraint(fields=['illustration', 'tag'], name='unique_illustration_tag')
            ]

    def __str__(self):
        return f'{self.illustration}, {self.tag}'
