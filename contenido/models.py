from django.db import models
from usuarios.models import Usuario


class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    autor = models.ForeignKey(Usuario, related_name='articulos', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    es_publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Revision(models.Model):
    articulo = models.ForeignKey(Articulo, related_name='revisiones', on_delete=models.CASCADE)
    revisor = models.ForeignKey(Usuario, related_name='revisiones_hechas', on_delete=models.CASCADE)
    fecha_revision = models.DateTimeField(auto_now_add=True)
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"{self.articulo.titulo} revisado por {self.revisor.email} el {self.fecha_revision}"


class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(Usuario, related_name='comentarios_hechos', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.email} en {self.articulo.titulo}"
