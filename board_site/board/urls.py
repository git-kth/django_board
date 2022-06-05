from django.urls import path

# from . import views
from .views import base_views, board_views, comment_views

app_name = 'board'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:board_id>/',base_views.detail , name="detail"),
    path('board_create/', board_views.board_create, name="board_create"),
    path('board_modify/<int:board_id>', board_views.board_modify, name="board_modify"),
    path('board_delete/<int:board_id>', board_views.board_delete, name="board_delete"),
    path('comment_create/<int:board_id>', comment_views.comment_create, name="comment_create"),
    path('comment_modify/<int:comment_id>', comment_views.comment_modify, name="comment_modify"),
    path('comment_delete/<int:comment_id>', comment_views.comment_delete, name="comment_delete"),
    # path('write/', views.write, name="write"),
    # path('add/',views.add, name ='add'),
    # path('delete/<int:idx>/',views.delete, name ="delete"),
    # path('update/<int:idx>/update_form',views.update_form , name = "update_form"),
    # path('update/<int:idx>',views.update , name = "update"),
    # path('page/<int:idx>/', views.paging, name="paging"),
    # path('comment_reg/<int:idx>/',views.comment_reg, name ="comment_reg"),
]