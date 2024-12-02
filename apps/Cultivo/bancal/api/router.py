from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.bancal.api.views import BancalViewSet

router = DefaultRouter()
router.register(r'bancales', BancalViewSet)

urlpatterns = [
    path('bancal', include(router.urls)),
]
