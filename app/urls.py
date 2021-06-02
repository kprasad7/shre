"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth_views
    
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , views.base , name="base"), 
    path('main/', views.frontpage, name='frontpage'),
    path('search/', views.search, name='search'),
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('add-product/', views.add_product, name='add_product'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
    path('<slug:category_slug>/', views.category, name='category'),
    path('logout', LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html'),name='adminlogin'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
