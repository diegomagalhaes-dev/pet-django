from django.contrib import admin

from appPetShop.models import Endereco, Cliente, Animal, Servico

admin.site.register(Endereco)
admin.site.register(Cliente)
admin.site.register(Animal)
admin.site.register(Servico)

