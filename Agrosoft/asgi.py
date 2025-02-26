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

from apps.Iot.datos_meteorologicos.api.routers import websocket_urlpatterns as meteo_ws

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(  # Agregamos AuthMiddlewareStack para WebSockets autenticados
        URLRouter(meteo_ws)
    ),
})