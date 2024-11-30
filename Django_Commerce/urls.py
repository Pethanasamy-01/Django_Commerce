"""
URL configuration for Django_Commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Commerce_App import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='Home'),
    path('register/',views.register,name='Register'),
    path('login/',views.login_view,name='Login'),
    path('all_products/',views.AllProducts.as_view(),name='All_Products'),
    path('create_product/',views.CreateProduct.as_view(),name='Create_Product'),
    path('wishlist_product/<int:id>',views.wishlist_product,name='Wishlist_Product'),
    path('wishlist_view/',views.wishlist_view,name='Wishlist_View'),
    path('wishlist_remove/<int:id>',views.wishlist_remove,name='Wishlist_Remove'),
    path('user_profile/',views.user_profile,name='User_Profile'),
    path('product_detail/<int:pk>/',views.Product_Detail.as_view(),name='Product_Detail'),
    path('order/<int:pk>/',views.order,name='Order'),
    path('logout/',views.logout_view,name='Logout'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
  urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)