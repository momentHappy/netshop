# coding=utf-8
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ToOrderView.as_view()),
    path('order.html', views.OrderListView.as_view()),
    # re_path(r'^category/(\d+)$', views.IndexView.as_view()),
    # re_path(r'^category/(\d+)/page/(\d+)$', views.IndexView.as_view()),
    # re_path(r'^goodsdetails/(\d+)$', views.DetailView.as_view())
]
