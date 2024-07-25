from django.shortcuts import render
from rest_framework import generics
from .models import Contact
from contact.serializers import ContactSerializer


class ContactCreateApiView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

