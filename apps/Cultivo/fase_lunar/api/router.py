from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.fase_lunar.api.views import FaseLunarViewSet

router = DefaultRouter()
router.register(r'fase_lunar', FaseLunarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
