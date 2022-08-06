
import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
import todoapp.routing
from channels.auth import AuthMiddleware
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')

application =ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(
        todoapp.routing.websocket_urlpatterns
    )
})
