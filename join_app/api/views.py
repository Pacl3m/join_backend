from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework import viewsets
from join_app.models import Card, Category, Contact
from .serializers import CardSerializer, CategorySerializer, ContactSerializer, RegistrationSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class ContactViewSet(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class CategoryViewSet(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def delete(self, request):
        Category.objects.all().delete()
        return Response()


class CustomLoginView(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, username=email, password=password)

        if user:
            return Response({"success": True, "email": user.email, "Vorname": user.first_name, "Nachname": user.last_name})
        else:
            return Response({"success": False, "message": "Falsche Login-Daten!"}, status=400)


class RegisterView(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            saved_account = serializer.save()

            return Response({
                "username": saved_account.username,
                "email": saved_account.email,
                "first_name": saved_account.first_name,
                "last_name": saved_account.last_name
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
