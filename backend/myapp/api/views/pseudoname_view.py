from rest_framework import viewsets

from myapp.api.serializers import PseudoNameSerializer

from myapp.models import PseudoName


class PseudoNameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pseudo names to be viewed or edited.
    """
    queryset = PseudoName.objects.all()
    serializer_class = PseudoNameSerializer
