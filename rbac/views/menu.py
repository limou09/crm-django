from django.shortcuts import render,redirect

from rbac import models
from rbac.forms.menuform import MenuModelForm


def menu_list(request):
    """
    菜单列表
    :param request:
    :return:
    """
    menu_queryset = models.Menu.objects.all()
    mid = request.GET.get('mid',1)
    sid = request.GET.get('sid',1)
    if mid:
        permission_queryset = models.Permission.objects.filter(menu_id=mid)
    else:
        permission_queryset = []
    if sid:
        parent_queryset = models.Permission.objects.filter(parent_id=sid)
    else:
        parent_queryset = []
    return render(request, 'rbac/menu_list.html', {
        'menu_queryset':menu_queryset,
        'permission_queryset':permission_queryset,
        'parent_queryset':parent_queryset,
    })


def menu_add(request):
    """
    添加菜单
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = MenuModelForm()
    else:
        form = MenuModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    return render(request, 'rbac/menu_add.html', {'form':form})


def menu_edit(request, mid):
    """
    菜单修改
    :param request:
    :param mid:
    :return:
    """
    obj = models.Menu.objects.get(id=mid)

    if request.method == 'GET':
        form = MenuModelForm(instance=obj)
    else:
        form = MenuModelForm(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    return render(request, 'rbac/role_edit.html', {'form':form})


def menu_del(request, mid):
    """
    删除菜单
    :param request:
    :param mid:
    :return:
    """
    models.Menu.objects.get(id=mid).delete()
    return redirect('menu_list')