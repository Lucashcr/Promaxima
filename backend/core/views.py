from rest_framework import viewsets

from .models import Medicamentos
from .serializers import MedicamentosSerializer

# Create your views here.


class MedicamentosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Medicamentos.objects.all()
    serializer_class = MedicamentosSerializer
