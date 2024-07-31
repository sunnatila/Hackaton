from rest_framework import generics, status
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer


class ContactCreateApiView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone', '')
        formatted_number = phone_number
        if not phone_number.startswith('+998'):
            formatted_number = '+998' + phone_number

        if Contact.objects.filter(phone=formatted_number).exists():
            return Response({"status": "Bu telefon raqamli foydalanuvchi mavjud."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GroupCreateApiView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
