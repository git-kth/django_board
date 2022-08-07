from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from ..models import Board
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def index(request):
    boards = Board.objects.order_by('-create_date')
    kw_type =request.GET.get('kw_type', '')
    kw = request.GET.get('kw', '')
    if kw:
        if kw_type == 'title':
            boards = boards.filter(
                Q(title__icontains=kw)
            ).distinct()
        elif kw_type == 'title_contents':
            boards = boards.filter(
                Q(title__icontains=kw) |
                Q(contents__icontains=kw)
            ).distinct()
        elif kw_type == 'user':
            boards = boards.filter(
                Q(user__username__icontains=kw)
            ).distinct()
    sorting = request.GET.get('sort', '')
    if sorting == 'reversed_id':
        boards = boards[::-1]
    elif sorting == 'view':
        boards = boards.order_by('-view')
    page = request.GET.get('page', 1)
    paginator = Paginator(boards, 10)
    page_obj = paginator.get_page(page)
    context = {'board_list': page_obj , 'sort': sorting, 'kw': kw, 'kw_type': kw_type}
    return render(request, 'board/board_list.html', context)

def detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    board.view += 1
    board.save()
    info = {'board': board}
    return render(request, 'board/board_detail.html', info)



