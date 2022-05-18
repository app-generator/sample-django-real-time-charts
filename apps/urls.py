from django.urls import path

from . import views
from apps.product.views import create_product, all_products

urlpatterns = [
    # The home page
    path("", views.index, name="home"),
    path("create/",create_product,name="create-product"),
    path("all/",all_products,name="all-products")
]