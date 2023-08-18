from django.contrib import admin

from garagem.models import Acessório, Categoria, Cor, Marca, Veiculo

admin.site.register(Acessório)
admin.site.register(Categoria)
admin.site.register(Cor)
admin.site.register(Marca)
admin.site.register(Veiculo)