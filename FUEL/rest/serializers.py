from rest_framework.serializers import ModelSerializer
from core.models import gasolina

class GasSerializer(ModelSerializer):
    class Meta:
        model = gasolina
        fields= '__all__'