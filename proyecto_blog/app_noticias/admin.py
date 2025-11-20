from django.contrib import admin
from .models import Noticias, Categorias

# Register your models here.

@admin.register(Noticias)
class NoticiasAdmin(admin.ModelAdmin):
    # agrega los campos que pasemos en la tupla
    list_display = ("titulo", "categoria", "fecha")
    #  filtra las noticias por categoria
    list_filter = ("categoria",)

    # cuadro de busqueda por campo que pasamos en la tupla
    search_fields = ("categoria",)

    
admin.site.register(Categorias)