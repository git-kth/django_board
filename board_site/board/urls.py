from django.urls import path

# from . import views
from .views import base_views, board_views, comment_views, mypage_views

app_name = 'board'

urlpatterns = [
    # base_views
    path('', base_views.index, name='index'),
    path('<int:board_id>/',base_views.detail , name="detail"),
    
    # board_views
    path('board_create/', board_views.board_create, name="board_create"),
    path('board_modify/<int:board_id>', board_views.board_modify, name="board_modify"),
    path('board_delete/<int:board_id>', board_views.board_delete, name="board_delete"),
    path('board_like/<int:board_id>', board_views.board_like, name="board_like"),
    path('board_unlike/<int:board_id>', board_views.board_unlike, name="board_unlike"),
    
    # comment_views
    path('comment_create/<int:board_id>', comment_views.comment_create, name="comment_create"),
    path('comment_modify/<int:comment_id>', comment_views.comment_modify, name="comment_modify"),
    path('comment_delete/<int:comment_id>', comment_views.comment_delete, name="comment_delete"),

    # mypage_views
    path('mypage_index/', mypage_views.mypage_index, name="mypage_index"),
]