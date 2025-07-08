from django.urls import path
from .views import UserListIteratorView


urlpatterns = [
    path('users', UserListIteratorView.as_view())


]