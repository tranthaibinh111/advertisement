from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'gio-hang/<int:sp_id>/', views.giohang, name='giohang'),
    path(r'hoan-tat/<int:or_id>/', views.hoantat, name='hoantat'),
    path(r'<str:sku>/<slug:slug>/', views.product, name='product'),
    path(r'chinh-sach-van-chuyen', views.vanchuyen, name='vanchuyen'),
    path(r'chinh-sach-doi-tra', views.doitra, name='doitra'),
    path(r'dieu-khoan-dieu-kien-thanh-toan', views.dieukhoanthanhtoan, name='dieukhoanthanhtoan'),
]
