"""Model representing the tags the Owner of portfolio's video may have."""

from django.db import models

from myapp.models import Skill, Tag


class SkillTag(models.Model):
    """
    Represents tags of Videos that is part of the Owner's portfolio.
    """
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    certificate = models.FileField(blank=True, null=True)

    def __str__(self):
        return f'{self.skill}, {self.tag}'
