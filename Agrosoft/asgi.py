import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import apps.Cultivo.actividades.api.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Agrosoft.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            apps.Cultivo.actividades.api.routing.websocket_urlpatterns
        )
    ),
})
