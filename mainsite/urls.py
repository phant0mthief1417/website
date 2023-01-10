from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('todo/', TaskList.as_view(), name="task"),
    path('todo/create/', TaskCreate.as_view(), name="create"),
    path('todo/login/', CustomLoginView.as_view(), name="login"),
    path('todo/logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('todo/register/', RegisterPage.as_view(), name="register"),
    path('todo/<int:pk>/', TaskDetail.as_view(), name="detail"),
    path('todo/update/<int:pk>/', TaskUpdate.as_view(), name="update"),
    path('todo/delete/<int:pk>/', TaskDelete.as_view(), name="delete"),
    path('home/', Home_page, name="Home_page"),
    path('asteroid/', Asteroid_page, name="Asteroid_page"),
]