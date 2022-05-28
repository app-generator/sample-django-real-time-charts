from channels.generic.websocket import WebsocketConsumer
from apps.product.models import Product
from apps.user.models import User
from asgiref.sync import async_to_sync
import calendar
import json



        
class SalesConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)('sales',self.channel_name)
        
        self.accept()
            
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
        
        async_to_sync(self.channel_layer.group_send)(
            'sales',
            {
                'type': 'send_data',
                'data':data
            }
        )
        
        
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)('sales',self.channel_name)
    
    def contact(self,event):
        self.send(json.dumps(event))
        
    def send_data(self,event):
        self.send(json.dumps(event))
        
    
    
        
        
class UserCreatedConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)('user',self.channel_name)
        self.accept()
        
        users = User.objects.all()
        months = []
        for user in users:
            months.append(user.created.date().month)
        months = list(set(months))
        months.sort()
        data = []
        for month in months:
            data.append({
                'month': calendar.month_name[month],
                'count': User.objects.filter(created__month=month).count()
            })
            
        async_to_sync(self.channel_layer.group_send)(
            'user',
            {
                'type': 'send_data',
                'data':data
            }
        )
        
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)('user',self.channel_name)
        
    def send_data(self,event):
        self.send(json.dumps(event))
     
       
class PurchaseStatConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)('user_purchase',self.channel_name)
        self.accept()
        
        users = User.objects.filter(has_purchased=True)
        response = [{
            'total_users': User.objects.count(),
            'total_purchased': users.count(),
            'purchased_percentage': round(users.count() / User.objects.count() * 100, 2)
        }]
        
        async_to_sync(self.channel_layer.group_send)(
            'user_purchase',
            {
                'type': 'send_data',
                'data':response
            }
        )
        
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)('user_purchase',self.channel_name)
        
    def send_data(self,event):
        self.send(json.dumps(event))
        
        
        
        
        
        

        
        
        
        
        

    
