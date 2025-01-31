from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('signup/', views.UserCreate.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('current/', views.UserRetrieveUpdateAPIView.as_view()),
 ]