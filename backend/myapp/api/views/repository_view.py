from rest_framework import viewsets

from myapp.api.serializers import RepositorySerializer

from myapp.models import Repository


class RepositoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows repositories to be viewed or edited.
    """
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
