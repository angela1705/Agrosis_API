from .views import SensoresViewset
from rest_framework.routers import DefaultRouter
from django.urls import re_path
from apps.Iot.sensores.api.consumer import SensoresConsumer

SensoresRouter = DefaultRouter()
SensoresRouter.register(prefix='sensores',viewset=SensoresViewset,basename='sensores')

websocket_urlpatterns = [
    re_path(r'ws/sensores/$', SensoresConsumer.as_asgi()),
]