from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticuloViewSet, RevisionViewSet, ComentarioViewSet

router = DefaultRouter()
router.register(r'articulos', ArticuloViewSet)
router.register(r'revisiones', RevisionViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
