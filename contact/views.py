from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .models import Contact
from contact.serializers import ContactSerializer


class ContactCreateApiView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        if Contact.objects.filter(phone=request.data['phone']).exists():
            raise ValidationError(detail={
                'status': 'Bu telefon raqamli kontakt mavjud.'
            })
        else:
            return super().post(request, *args, **kwargs)

