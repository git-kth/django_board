from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponseNotAllowed

from board.models import Comment, Board
from board.forms import CommentForm

@login_required(login_url='account:login')
def comment_create(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()
            comment.user = request.user
            comment.board = board
            comment.save()
            return redirect('board:detail', board_id=board.id)
    else:
        return HttpResponseNotAllowed('오직 POST방식만 가능합니다.')
    context = {'board': board, 'form': form}
    return render(request, 'board/comment_form.html', context)

login_required(login_url='account:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.user != request.user:
        messages.error(request, '답글의 수정권한이 없습니다.')
        return redirect('board:detail', board_id=comment.board.id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('board:detail', board_id=comment.board.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'board/comment_form.html', context)

login_required(login_url='account:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.user:
        messages.error(request, '답글의 삭제권한이 없습니다.')
    else:
        comment.delete()
    return redirect('board:detail', board_id=comment.board.id)
