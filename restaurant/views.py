from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class BookingView(generics.ListCreateAPIView):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer