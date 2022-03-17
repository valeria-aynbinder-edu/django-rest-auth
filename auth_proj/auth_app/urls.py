from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("public/", views.public_view),
    path("private/", views.private_view),
    path('api-token-auth/', obtain_auth_token),
    path('signout/', views.sign_out),
]