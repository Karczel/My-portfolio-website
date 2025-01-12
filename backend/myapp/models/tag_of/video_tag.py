"""Model representing the tags the Owner of portfolio's video may have."""

from django.db import models

from myapp.models import Video, Tag


class VideoTag(models.Model):
    """
    Represents tags of Videos that is part of the Owner's portfolio.
    """
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    class Meta:
            constraints = [
                models.UniqueConstraint(fields=['video', 'tag'], name='unique_video_tag')
            ]

    def __str__(self):
        return f'{self.video}, {self.tag}'
