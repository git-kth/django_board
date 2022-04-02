from django.shortcuts import render, redirect
from django.utils import timezone
from board.models import Board
from django.core.paginator import Paginator

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
    board_obj = Board.objects.get(id=idx)
    board_obj.view += 1
    board_obj.save()
    info = {'board_obj': board_obj}
    return render(request, 'board/view.html', info)

def add(request):
    board = Board()
    board.name = request.POST['name']
    board.title = request.POST['title']
    board.contents = request.POST['contents']
    board.create_date = timezone.now()
    board.update_date = timezone.now()
    board.view = 0
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