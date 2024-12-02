from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.especies.api.views import EspecieViewSet

router = DefaultRouter()
router.register(r'especies', EspecieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
