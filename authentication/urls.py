from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

app_name = 'authentication'

urlpatterns = [
    path('api/auth/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/auth/register/', views.CreateUserView.as_view(), name='auth_register'),
]
