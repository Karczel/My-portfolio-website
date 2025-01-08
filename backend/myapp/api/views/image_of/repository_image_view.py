from rest_framework import viewsets

from myapp.api.serializers import RepositoryImageSerializer

from myapp.models import RepositoryImage


class RepositoryImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow repository images to be viewed or edited.
    """
    queryset = RepositoryImage.objects.all()
    serializer_class = RepositoryImageSerializer
