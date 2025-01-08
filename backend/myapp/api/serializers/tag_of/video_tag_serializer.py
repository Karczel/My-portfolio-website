from myapp.models import VideoTag
from rest_framework import serializers


class VideoTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoTag
        fields = '__all__'
