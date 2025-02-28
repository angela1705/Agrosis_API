"""
ASGI config for Agrosis project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Agrosoft.settings')
django.setup()

from apps.Iot.sensores.api.routers import websocket_urlpatterns as sensores_ws
from apps.Cultivo.actividades.api.routing import websocket_urlpatterns as actividades_ws

combined_ws_urlpatterns = sensores_ws + actividades_ws

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(combined_ws_urlpatterns)
    ),
})
