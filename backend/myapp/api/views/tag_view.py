from rest_framework import viewsets

from myapp.api.serializers import TagSerializer

from myapp.models import Tag


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
