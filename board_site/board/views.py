from django.shortcuts import render
from board.models import Board

def index_board(request):
    board_obj = Board.objects.all()
    reversed_board_obj = board_obj[::-1]
    info = {'reversed_board_obj': reversed_board_obj}
    return render(request, 'board.html', info)

def index_board_write(request):
    return render(request, 'board_write.html')

def index_board_view(request):
    return render(request, 'board_view.html')

def detail(request, idx):
    board_obj = Board.objects.get(id=idx)
    info = {'board_obj': board_obj}
    return render(request, 'board_view.html', info)