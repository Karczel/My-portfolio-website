from rest_framework import viewsets

from myapp.api.serializers import ActivityImageSerializer

from myapp.models import ActivityImage


class ActivityImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows activity images to be viewed or edited.
    """
    queryset = ActivityImage.objects.all()
    serializer_class = ActivityImageSerializer
