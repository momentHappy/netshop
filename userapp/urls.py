# coding=utf-8
from django.urls import path, re_path
from . import views

urlpatterns = (
    path('register/', views.RegisterView.as_view()),
    path('checkUname/', views.CheckUnameView.as_view()),
    path('center/', views.CenterView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('loadCode.jpg', views.LoadCodeView.as_view()),
    path('checkcode/', views.CheckcodeView.as_view()),
    path('address/', views.AddressView.as_view()),
    path('loadArea/', views.LoadAreaView.as_view()),

    # re_path(r'^category/(\d+)$', views.IndexView.as_view()),
    # re_path(r'^category/(\d+)/page/(\d+)$', views.IndexView.as_view()),
    # re_path(r'^goodsdetails/(\d+)$', views.DetailView.as_view())
)
