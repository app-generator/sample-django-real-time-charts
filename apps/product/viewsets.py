import calendar

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from apps.product.models import Product
from apps.product.serializers import ProductSerializer

channel_layer = get_channel_layer()

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'], url_path='sales')
    def sales_over_month(self, request, *args, **kwargs):
        if request.method == 'POST':
            products = Product.objects.none()
        months = []
        for product in products:
            months.append(product.created.date().month)
        months = list(set(months))
        months.sort()
        data = []
        for month in months:
            data.append({
                'month': calendar.month_name[month],
                'count': Product.objects.filter(created__month=month).count()
            })
    
        else:
            products = Product.objects.none()
            months = []
            for product in products:
                months.append(product.created.date().month)
            months = list(set(months))
            months.sort()
            data = []
            for month in months:
                data.append({
                    'month': calendar.month_name[month],
                    'count': Product.objects.filter(created__month=month).count()
                })
                

            return Response(data, status=status.HTTP_200_OK)
    
    def get_queryset(self):
        products = Product.objects.all()
        months = []
        for product in products:
            months.append(product.created.date().month)
        months = list(set(months))
        months.sort()
        data = []
        for month in months:
            data.append({
                'month': calendar.month_name[month],
                'count': Product.objects.filter(created__month=month).count()
            })
        return Product.objects.filter(created__month=month)            
    