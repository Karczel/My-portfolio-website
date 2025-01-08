"""Model for owner's Repositories"""

from django.db import models
# repo link, preview image


class Repository(models.Model):
    """
    Represents activity of Owner of the portfolio.
    Contain Information of the activity project to display while the activity is contained elsewhere.
    """
    name = models.TextField()
    desc = models.TextField(blank=True, null=True)
    link = models.TextField()
    product = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
