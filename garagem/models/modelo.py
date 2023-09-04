from django.db import models
    
class Modelo(models.Model):
    Categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="modelo")
    Marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="modelo")
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome