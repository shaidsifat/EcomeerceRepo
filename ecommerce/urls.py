"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from product.views import  ProductList,ProductSearchlist,ProductOrderPost,Userlist,Orderlist,OrdertStatusUpdatelist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/productlist/', ProductList.as_view(),name='productlist'),
    path('api/product/search/details/<int:pk>/',ProductSearchlist.as_view(),name='searchlist',),
    path('api/product/order/',ProductOrderPost.as_view(),name='ProductOrderPost'),
    path('api/userlist/admin/',Userlist.as_view(),name='Userlist'),
    path('api/orderlist/admin',Orderlist.as_view(),name='Orderlist'),
    path('api/orderupdate/admin',OrdertStatusUpdatelist.as_view(),name='OrdertStatusUpdatelist')
]
