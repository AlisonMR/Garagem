from django.db import models

class Acessório(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.upper()

class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    descricao = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")
    descricao = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    nome = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.CharField(max_length=32, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)

    def __str__(self):
        return self.nome