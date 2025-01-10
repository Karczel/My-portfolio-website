"""Model for portfolio Owner's skills."""

from django.db import models
# additional or main type
from myapp.utils import NAME


class Skill(models.Model):
    """
    Represent skills of the Owner of portfolio.
    """
    skill = models.CharField(max_length=NAME)
    type = models.CharField(max_length=NAME,
                            choices=[
                                ('main', 'Main'),
                                ('additional', 'Additional')
                            ],
                            default='main')

    def __str__(self):
        return self.skill
