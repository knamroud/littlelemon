from django.urls import path
from . import views


urlpatterns = [
    path("api/register", views.RegisterView.as_view()),
    path("api/login", views.LoginView.as_view()),
    path("api/logout", views.LogoutView.as_view()),
    path("api/me", views.MeView.as_view()),
]
