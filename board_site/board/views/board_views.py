from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from board.forms import BoardForm
from board.models import Board
from django.contrib.auth.decorators import login_required

@login_required(login_url='account:login')
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.create_date = timezone.now()
            board.view = 0
            board.user = request.user
            board.save()
            return redirect('board:detail', board_id=board.id)
    else:
        form = BoardForm()
    return render(request, 'board/board_form.html', {'form': form})

@login_required(login_url='account:login')
def board_modify(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.user != board.user:
        messages.error(request, '게시글의 수정권한이 없습니다.')
        return redirect('board:detail', board_id=board.id)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.modify_date = timezone.now()
            board.save()
            return redirect('board:detail', board_id=board.id)
    else:
        form = BoardForm(instance=board)
    return render(request, 'board/board_form.html', {'form': form})

@login_required(login_url='account:login')
def board_delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.user != board.user:
        messages.error(request, '게시글의 삭제권한이 없습니다.')
        return redirect('board:detail', board_id=board.id)
    board.delete()
    return redirect('board:index')

@login_required(login_url='account:login')
def board_like(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if not request.user in board.unlike.all:
        board.like.add(request.user)

    return redirect('board:detail', board_id)


@login_required(login_url='account:login')
def board_unlike(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if not request.user in board.like.all:
        board.unlike.add(request.user)

    return redirect('board:detail', board_id)
