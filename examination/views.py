from rest_framework import viewsets
from .models import Diagnostics
from .serializers import DiagnosticsSerializer


class DiagnosticsViewSet(viewsets.ModelViewSet):
    serializer_class = DiagnosticsSerializer
    queryset = Diagnostics.objects.all()
