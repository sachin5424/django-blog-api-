from django.shortcuts import render
from  rest_framework import generics
from .serializers import blogSerializer,categorieSerializer,blogSerializerCreate,contactSerializer
from .models import BLOG,Categories,Contact
from rest_framework.pagination import BasePagination
# Create your views here.

class Categories_ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = categorieSerializer



class Categories_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = categorieSerializer




class BlogView(generics.ListAPIView):
    queryset = BLOG.objects.all()
    serializer_class = blogSerializer


class BlogView1(generics.ListCreateAPIView):
    queryset = BLOG.objects.all()
    serializer_class = blogSerializerCreate







class Contact_Create_View(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = contactSerializer


class Contact_RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = contactSerializer

