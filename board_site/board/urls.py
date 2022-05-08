from django.urls import path

from . import views

app_name = 'board'
urlpatterns = [
    path('', views.index, name="index"),
    path('<str:sort>', views.index, name="index"),
    path('write/', views.write, name="write"),
    path('detail/<int:idx>/',views.detail , name="detail"),
    path('add/',views.add, name ='add'),
    path('delete/<int:idx>/',views.delete, name ="delete"),
    path('update/<int:idx>/update_form',views.update_form , name = "update_form"),
    path('update/<int:idx>',views.update , name = "update"),
    path('page/<int:idx>/', views.paging, name="paging"),
    path('comment_reg/<int:idx>/',views.comment_reg, name ="comment_reg"),
]