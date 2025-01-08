from rest_framework import viewsets

from myapp.api.serializers import IllustrationSerializer

from myapp.models import Illustration


class IllustrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows illustrations to be viewed or edited.
    """
    queryset = Illustration.objects.all()
    serializer_class = IllustrationSerializer
