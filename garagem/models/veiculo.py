from django.db import models

from garagem.models import Acessorio, Modelo, Cor


class Veiculo(models.Model):
    Acessorio = models.ForeignKey(Acessorio, on_delete=models.PROTECT, related_name="veiculos")
    Modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    Cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.CharField(max_length=32, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao