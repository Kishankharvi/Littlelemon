from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from .serializers import MenuItemSerializer
from .models import MenuItem




from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
#@authentication_classes([TokenAuthentication])
def msg(request):
    if request.method == 'POST':
        return Response({"message": "This is a POST request with CSRF protection"})
    return Response({"message": "This view is protected"})
 

# Create your views here.
class  MenuItemView(ListCreateAPIView):
  #  permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
class  SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    