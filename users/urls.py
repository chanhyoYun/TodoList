from django.contrib import admin
from django.urls import path, include
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'users'

urlpatterns = [
    path('log/', views.UserView.as_view(), name='user_view'), # 회원가입
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), # 토큰방식 로그인
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:user_id>/', views.UserDetailView.as_view(), name='user_detail'),
]
