from django.shortcuts import render
from board.models import Board

def index(request):
    board_obj = Board.objects.all()
    reversed_board_obj = board_obj[::-1]
    info = {'reversed_board_obj': reversed_board_obj}
    return render(request, 'board/index.html', info)

def write(request):
    return render(request, 'board/write.html')

def view(request):
    return render(request, 'board/view.html')

def detail(request, idx):
    board_obj = Board.objects.get(id=idx)
    info = {'board_obj': board_obj}
    return render(request, 'board/view.html', info)