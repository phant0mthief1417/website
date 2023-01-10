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
    path('', Home_page, name="Home_page"),
    path('home/', Home_page, name="Home_page"),
    path('asteroid/', Asteroid_page, name="Asteroid_page"),
    path('maze/', Maze_page, name="Maze_page"),
    path('fireworks/', Fireworks_page, name="Fireworks_page"),
    path('salesman/', Salesman_page, name="Salesman_page"),
    path('minesweeper/', Mine_page, name="Mine_page"),
]
