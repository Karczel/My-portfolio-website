from rest_framework import viewsets

from myapp.api.serializers import VideoSerializer

from myapp.models import Video


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows videos to be viewed or edited.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
