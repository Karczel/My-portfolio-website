from rest_framework import viewsets

from myapp.api.serializers import IllustrationTagSerializer

from myapp.models import IllustrationTag


class IllustrationTagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow illustration tags owners to be viewed or edited.
    """
    queryset = IllustrationTag.objects.all()
    serializer_class = IllustrationTagSerializer
