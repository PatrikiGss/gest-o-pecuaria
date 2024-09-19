from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]