from django.urls import path
from .views import user_list_create
from .views import login_user

urlpatterns = [
    path('auth/', user_list_create, name="user_list_create"),
    path('api/user/login/', login_user),
]
