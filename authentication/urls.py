from django.urls import path 
from . import views
from .views import RegisterView , CustomTokenObtainPairView , UserProfileView , LogoutView  
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # تسجيل الدخول باستخدام email أو username
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # تحديث التوكن
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', UserProfileView.as_view(), name='user_profile'),

]

