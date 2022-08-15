import imp
from django.shortcuts import render
from board.models import Board
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User

@login_required(login_url='account:login')
@permission_required('board.manager', raise_exception=False, login_url='board:mypage_index')
def manage_index(request):
    user_list = User.objects.order_by('username').filter(
        ~Q(user_permissions__codename='manager') & ~Q(is_superuser=True)
    ).distinct()

    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 10)
    page_obj = paginator.get_page(page)

    return render(request, 'board/manage.html', {'user_list':page_obj})

