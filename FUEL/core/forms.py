from django import forms
from .models import gasolina
from django.http.response import JsonResponse

class GasForm(forms.ModelForm):
    class Meta:
        model = gasolina
        fields = ['tipo','litros_vendidos']
        
        def get(self,request):
           gas=gasolina.tipo
           if len(gas)>0:
              datos={'message': 'Success','gas':gas}
           else:
              datos={'message': 'Gas not found'}
           return JsonResponse(datos)
           