from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'chinh-sach-van-chuyen', views.vanchuyen, name='vanchuyen'),
    path(r'chinh-sach-doi-tra', views.doitra, name='doitra'),
    path(r'gio-hang/<int:sp_id>/', views.giohang, name='giohang'),
    path(r'thanh-toan', views.thanhtoan, name='thanhtoan'),
    path(r'hoan-tat', views.hoantat, name='hoantat'),
]
