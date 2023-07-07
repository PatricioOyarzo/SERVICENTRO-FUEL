from django.db import models

# Create your models here.
class gasolina(models.Model):
    tipo = models.CharField(max_length=100)
    litros_vendidos = models.DecimalField(max_digits=10, decimal_places=2)
    monto_litro = models.DecimalField(max_digits=10, decimal_places=2)
    
    def calculo_valor(self):
        return int(self.litros_vendidos * self.monto_litro)