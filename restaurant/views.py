from django.shortcuts import render
from rest_framework import generics, permissions
from . import models
from . import serializers
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

    def get_permissions(self):
        return [permissions.IsAuthenticated() if self.request.method == "GET" else permissions.IsAdminUser()]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

    def get_permissions(self):
        return [permissions.IsAuthenticated() if self.request.method == "GET" else permissions.IsAdminUser()]


class BookingView(generics.ListCreateAPIView):
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Booking.objects.all() if self.request.user.is_superuser else models.Booking.objects.all().filter(user=self.request.user)
