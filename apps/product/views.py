from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
import calendar

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


channel_layer = get_channel_layer()


def sales_over_month():
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
        print('response')
        async_to_sync(channel_layer.group_send)(
            'sales',
            {
                'type': 'send_data',
                'data':data
            }
        )
        

@api_view(['POST'])
def create_product(request):
    product = ProductSerializer(data=request.data)
    
    if product.is_valid():
        product.save()
        sales_over_month()
        print('called')
        return Response(product.data)
    else:
        return Response(status_code=status.HTTP_400_NOT_FOUND)
    

@api_view(['GET'])
def all_products(request):
    products = Product.objects.all()
    if products:
        products = ProductSerializer(products,many=True)
        
        return Response(products.data)
    else:
        return Response(status_code=status.HTTP_400_NOT_FOUND)
    