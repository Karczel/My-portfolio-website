from rest_framework import viewsets

from myapp.api.serializers import SkillSerializer

from myapp.models import Skill


class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows skills to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
