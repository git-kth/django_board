from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from board.models import Board, Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request, sort='id'):
    a = Board.objects.all()

    if sort == 'id':
        sorted_obj = a[::-1]
    elif sort == 'reverse_id':
        sorted_obj = a
    elif sort == 'view':
        sorted_obj = a.order_by('-view')

    paginator = Paginator(sorted_obj, 10)
    board_obj = paginator.get_page(1)

    info = {'board_obj': board_obj}
    return render(request, 'board/index.html', info)

def write(request):
    return render(request, 'board/write.html')

def detail(request, idx):
    board_obj = get_object_or_404(Board, pk=idx)
    board_obj.view += 1
    board_obj.save()
    info = {'board_obj': board_obj}
    return render(request, 'board/view.html', info)

@login_required(login_url='account:login')
def add(request):
    board = Board()
    board.title = request.POST['title']
    board.contents = request.POST['contents']
    board.create_date = timezone.now()
    board.update_date = timezone.now()
    board.view = 0
    board.user = request.user
    board.save()
    return redirect('board:index')

def delete(request , idx):
    Board.objects.get(id = idx).delete()
    return redirect('board:index')

def update_form(request , idx):
    board_obj = Board.objects.get(id = idx)
    return render(request , 'board/write.html',{'board_obj' : board_obj})

def update(request , idx):
    board_obj = Board.objects.get(id = idx)
    board_obj.title = request.POST['title']
    board_obj.contents = request.POST['contents']
    board_obj.update_date = timezone.now()
    board_obj.save()
    return render(request , 'board/view.html' , {'board_obj':board_obj})

def paging(request, idx):
    a = Board.objects.all()
    reversed_board_obj = a[::-1]
    paginator = Paginator(reversed_board_obj, 10)
    board_obj = paginator.get_page(idx)
    info = {'board_obj': board_obj}
    return render(request, 'board/index.html', info)

def comment_reg(request, idx):
    board = get_object_or_404(Board, pk=idx)
    comment = Comment()
    comment.user = request.user
    comment.contents = request.POST['comment_text']
    # comment.reg_date = timezone.now()
    # comment.source_number = idx
    comment.board = board
    comment.save()
    return redirect('board:detail', idx=board.id)