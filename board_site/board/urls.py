from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_board, name="index_board"),
    path('board_write/', views.index_board_write, name="index_board_write"),
    path('<int:idx>/',views.detail , name = "detail")
]