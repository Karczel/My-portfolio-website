"""Model representing Owner of the portfolio."""

from django.db import models
from django.contrib.auth.models import User


class Owner(User):
    """
    Represents Owner for this version of portfolio has only one entity, this is for extending User class to add more details of
    Owner that may be relevant as Portfolio for job application.
    """
    quote = models.TextField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True)
    resume = models.FileField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Owner"
        verbose_name_plural = "Owners"

    def __str__(self):
        """Return the username of the owner."""
        return self.username

