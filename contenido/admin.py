from django.contrib import admin
from .models import Articulo, Revision, Comentario


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion', 'fecha_modificacion', 'es_publicado')
    list_filter = ('fecha_creacion', 'es_publicado')
    search_fields = ('titulo', 'contenido')


class RevisionAdmin(admin.ModelAdmin):
    list_display = ('articulo', 'revisor', 'fecha_revision')
    list_filter = ('fecha_revision',)
    search_fields = ('articulo__titulo', 'comentarios')


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('articulo', 'autor', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('articulo__titulo', 'contenido')


admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Revision, RevisionAdmin)
admin.site.register(Comentario, ComentarioAdmin)
