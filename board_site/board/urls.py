from django.urls import path

# from . import views
from .views import base_views, board_views, comment_views

app_name = 'board'

urlpatterns = [
    # base_views
    path('', base_views.index, name='index'),
    path('<int:board_id>/',base_views.detail , name="detail"),
    
    # board_views
    path('board_create/', board_views.board_create, name="board_create"),
    path('board_modify/<int:board_id>', board_views.board_modify, name="board_modify"),
    path('board_delete/<int:board_id>', board_views.board_delete, name="board_delete"),
    
    # comment_views
    path('comment_create/<int:board_id>', comment_views.comment_create, name="comment_create"),
    path('comment_modify/<int:comment_id>', comment_views.comment_modify, name="comment_modify"),
    path('comment_delete/<int:comment_id>', comment_views.comment_delete, name="comment_delete"),
]