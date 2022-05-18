from django.urls import path
from .consumers import SalesConsumer, UserCreatedConsumer, PurchaseStatConsumer


ws_urlpatterns = [
    path('ws/products/',SalesConsumer.as_asgi()),
    path('ws/users-purchased/',PurchaseStatConsumer.as_asgi()),
    path('ws/users-created/',UserCreatedConsumer.as_asgi())

]