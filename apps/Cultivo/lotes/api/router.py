from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.lotes.api.views import LoteViewSet

router = DefaultRouter()
router.register(r'lotes', LoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
