"""Tags for search engine within portfolio."""

from django.db import models

from myapp.utils import NAME


class Tag(models.Model):
    """
    Works of user could use tags to categorize their work and makes it easier to search for employers.
    """
    content = models.CharField(max_length=NAME)

    def __str__(self):
        return self.content
