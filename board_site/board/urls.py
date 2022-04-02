from django.urls import path

from . import views

app_name = 'board'
urlpatterns = [
    path('', views.index, name="index"),
    path('board_write/', views.write, name="write"),
    path('<int:idx>/',views.detail , name="detail")
]