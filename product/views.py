from django.shortcuts import render
from .models import product
from rest_framework import generics
from product.serializers import SnippetSerializer,OrderSerializer,UserListSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.models import  product
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

class ProductList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        snippets = product.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

  

class ProductSearchlist(APIView):

    permission_classes = [IsAuthenticated]    

    def get(self,request,pk,format=None):
        snippet = product.objects.filter(Q(name__icontains=pk) | Q(id=pk))  
        serializer = SnippetSerializer(snippet, many=True)

        return Response(serializer.data)

class ProductOrderPost(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request,format=None):

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class Userlist(APIView):

    permission_classes = [IsAdminUser]   
    def get(self,request):

       query =  User.objects.all()
       serializer = UserListSerializer(query, many=True)
       return Response(serializer.data)

class Orderlist(APIView):
    permission_classes = [IsAdminUser]   
    def get(self,request):

        query = Order.objects.all()
        serializer = OrderSerializer(query,many=True)  
        return Response(serializer.data)   

class OrdertStatusUpdatelist(APIView):

    permission_classes = [IsAdminUser]   
    def get_object(self, pk):

        try:
            return Order.objects.get(id=pk)
        except Order.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = OrderSerializer(snippet, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
