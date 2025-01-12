from rest_framework import viewsets

from myapp.api.serializers import SkillTagSerializer

from myapp.models import SkillTag


class SkillTagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows skill tags to be viewed or edited.
    """
    queryset = SkillTag.objects.all()
    serializer_class = SkillTagSerializer
