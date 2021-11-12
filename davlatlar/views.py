from rest_framework import viewsets
from .serializers import CountrySerializer
from .models import Countries


class CountryViewset(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountrySerializer
