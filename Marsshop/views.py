from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from app.serializer import *
import random
# Create your views here.
class ProductView(APIView):
    def get(self, request):
        Products = Product.objects.all()
        if Products:
            serializer = ProductSRL(Products, many = True)
            return Response(serializer.data)
        else:
            return Response ('Bizda hozircha mahsulotlar yoq')
        
    def post(self, request):
        serializer = ProductSRL(data= request.data)
        if serializer.id_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class EditProductView(APIView):

    def get (self, request, id):
        Product = Product.objects.filter(id=id).firts()
        if Product:
            serializer = ProductSRL(Product)
            return Response(serializer.data)
        else:
            return Response("Bunday mahsulot topilmadi")
        

    def get (self, request, id):
        Product = Product.objects.filter(id=id).firts()
        if Product:
            serializer = ProductSRL(instance=Product, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save() 
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Bunday mahsulot topilmadi")

    def delete(self, request, id):
        Product = Product.objetcs.filter(id=id).first()
        if Product:
           Product.delete()
           return Response("O'chirildi")
        else:
            return Response("Bunday Mahsulot topilmadi")

    
class ProductOrderView(APIView):
    def post(self, request):
        product = request.data.get('product')
        products = Product.objects.all()
        quantity_order = request.data.get('quantity')
        if product in products:
            for product in products:
                if product == product and quantity_order <= product.quantitiy:
                    serializer =  OrderSRL(data = request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    else:
                        return Response(serializer.errors)
                else:
                    continue
            else:
                return Response("Bizda bunday mahsulot mavjud emas")

def cod():
    return random.randit(1000, 9999) 


class PostOrderView(APIView):
    def post(self, request, id):
        product= Product.objects.filter(id=id).first()
        if product:
            quantity = request.data.get('quantity')
            if product.quantitiy <= quantity:
                a = cod()
                return Response("Haridingiz uchun rahmat")
            else:
                return Response ("Xatolik yuz berdi")
    


class GetOrderView(APIView):
    def get(self, request, id):
        user = User.objects.filter(id = id).first()
        if user:
            order = Order.objects.filter(user=user)
            serializers = OrderSRL(order, many=True)
            return Response(serializers.data)
        else:
            return Response("Bunday user mavjud emas")