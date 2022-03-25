from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from api.serializers import ProductSerializer
from api.models import Products

# Create your views here.
class ListProductAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class CreateProductAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class UpdateProductAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class DeleteProductAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer