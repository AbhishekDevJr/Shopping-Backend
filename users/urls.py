from django.urls import path
from .views import RegistrationView, LoginView, LogoutView

urlpatterns = [
    path('registration', RegistrationView.as_view(), name='user-registration'),
    path('login', LoginView.as_view(), name='user-login'),
    path('logout', LogoutView.as_view(), name='user-logout')
]
