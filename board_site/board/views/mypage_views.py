from django.shortcuts import get_object_or_404, render, redirect
from board.models import Board
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User

@login_required(login_url='account:login')
def mypage_index(request):
    if request.user.has_perm('board.manager'):
        user_id = request.GET.get('user_id', '')
        if user_id:
            user = get_object_or_404(User, pk=user_id)
        else:
            return redirect('board:manage_index')
    else:
        user = request.user
    type = request.GET.get('type', 'like')
    if type == 'unlike':
        board_list = user.unlike_user.all()
    else:
        board_list = user.like_user.all()

    kw_type =request.GET.get('kw_type', '')
    kw = request.GET.get('kw', '')
    if kw:
        if kw_type == 'title':
            board_list = board_list.filter(
                Q(title__icontains=kw)
            ).distinct()
        elif kw_type == 'title_contents':
            board_list = board_list.filter(
                Q(title__icontains=kw) |
                Q(contents__icontains=kw)
            ).distinct()
        elif kw_type == 'user':
            board_list = board_list.filter(
                Q(user__username__icontains=kw)
            ).distinct()

    board_list = board_list.order_by('-create_date')

    page = request.GET.get('page', 1)
    paginator = Paginator(board_list, 10)
    page_obj = paginator.get_page(page)
    context = {'board_list': page_obj , 'kw': kw, 'kw_type': kw_type, 'type': type, 'user_id': user.id,}

    return render(request, 'board/mypage_index.html', context)