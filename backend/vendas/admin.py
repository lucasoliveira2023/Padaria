from django.contrib import admin

from vendas.models import ItemVenda, Vendas

admin.site.register(Vendas)
admin.site.register(ItemVenda)
