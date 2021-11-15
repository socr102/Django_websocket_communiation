"""
ASGI config for websocket_example project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_example.settings')

from django.core.asgi import get_asgi_application

from websocket.middleware import websockets

application = get_asgi_application()

application = websockets(application)

