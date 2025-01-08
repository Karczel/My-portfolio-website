from rest_framework import viewsets

from myapp.api.serializers import ContactSerializer

from myapp.models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows owners to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
