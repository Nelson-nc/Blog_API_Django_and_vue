from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("api/account/", views.accountOverView, name="account_overview"),
    path("api/account/register", views.registerView, name="account_register"),
    path("api/account/login", TokenObtainPairView.as_view(), name="account_login"),
    path("api/account/refresh", TokenRefreshView.as_view(), name="account_refresh"),
    path("api/account/dashboard", views.dashboardView, name="dashboard"),
    path("api/account/dashboard/update", views.updateSelfView, name="update_account"),
    path("api/account/dashboard/delete", views.dashboardView, name="delete_account"),
    path("api/account/user/<int:pk>", views.getUserView, name="get_user"),
]