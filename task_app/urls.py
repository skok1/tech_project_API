from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('api/v1/task/', TaskCreateAPI.as_view()),
    path('api/v1/task/<int:pk>/', TaskUpdateAPI.as_view()),
    path('api/v1/task/<int:pk>/delete/', TaskDeleteAPI.as_view()),
    path('api/v1/category/', CategoryCreateAPI.as_view()),
    path('api/v1/category/<int:pk>/', CategoryUpdateAPI.as_view()),
    path('api/v1/category/<int:pk>/delete/', CategoryDeleteAPI.as_view()),
    path('api/v1/session_auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
