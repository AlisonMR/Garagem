from django.db import models
from uploader.models import Image
from garagem.models import Acessorio, Modelo, Cor


class Veiculo(models.Model):
    acessorio = models.ManyToManyField(Acessorio, related_name="veiculos")
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.CharField(max_length=32, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    descricao = models.CharField(max_length=50)
    capa = models.ManyToManyField(Image, related_name="+")

    def __str__(self):
        return self.descricao