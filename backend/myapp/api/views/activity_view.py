from rest_framework import viewsets

from myapp.api.serializers import ActivitySerializer

from myapp.models import Activity


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows activities to be viewed or edited.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
