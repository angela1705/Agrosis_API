from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.plagas.api.views import PlagaViewSet

router = DefaultRouter()
router.register(r'plagas', PlagaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
