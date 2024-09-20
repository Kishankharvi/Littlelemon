from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import MenuSerializer,BookingSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Menu,Booking
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
# Create your views here


                  
def index(request):
    return render(request, 'index.html', {})

class  MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
class  SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class=BookingSerializer

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer