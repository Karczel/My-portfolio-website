from rest_framework import viewsets

from myapp.api.serializers import RepositoryTagSerializer

from myapp.models import RepositoryTag


class RepositoryTagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows repository tags to be viewed or edited.
    """
    queryset = RepositoryTag.objects.all()
    serializer_class = RepositoryTagSerializer
