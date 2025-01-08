from rest_framework import viewsets

from myapp.api.serializers import OwnerSerializer

from myapp.models import Owner


class OwnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows owners to be viewed or edited.
    """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
