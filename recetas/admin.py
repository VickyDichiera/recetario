from django.contrib import admin

from .models import Receta, MateriaPrima, Ingrediente

admin.site.register(Receta)
admin.site.register(MateriaPrima)
admin.site.register(Ingrediente)
