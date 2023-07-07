from rest_framework.viewsets import ModelViewSet
from core.models import gasolina
from rest.serializers import GasSerializer

# Create your views here.

class GasApiViewSet(ModelViewSet):
    queryset = gasolina.objects.all()
    serializer_class= GasSerializer