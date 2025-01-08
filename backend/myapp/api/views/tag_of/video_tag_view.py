from rest_framework import viewsets

from myapp.api.serializers import VideoTagSerializer

from myapp.models import VideoTag


class VideoTagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows video tags to be viewed or edited.
    """
    queryset = VideoTag.objects.all()
    serializer_class = VideoTagSerializer
