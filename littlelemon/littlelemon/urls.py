#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views
router=DefaultRouter()
router.register(r'tables',views.BookingViewSet)


urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/',include('LittleLemonAPI.urls')),
   
   path('restaurant/', include("restaurant.urls")),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('restaurant/menu/',include('restaurant.urls')),
   path('restaurant/booking/', include(router.urls)),
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.authtoken')),
]
