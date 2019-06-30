from django.shortcuts import render, redirect
from rbac import models
from rbac.forms.roleform import RoleModelForm

def role_list(request):
    """
    角色列表
    :param request:
    :return:
    """
    role_queryset = models.Role.objects.all()
    return render(request, 'rbac/role_list.html', {'role_queryset':role_queryset})


def role_add(request):
    """
    添加角色
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = RoleModelForm()
    else:
        form = RoleModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/rbac/role/list/')
    return render(request, 'rbac/role_add.html', {'form':form})


def role_edit(request, rid):
    """
    角色修改
    :param request:
    :return:
    """
    obj = models.Role.objects.filter(id=rid).first()
    if request.method == 'GET':
        form = RoleModelForm(instance=obj)
    else:
        form = RoleModelForm(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    return render(request, 'rbac/role_edit.html', {'form':form})


def role_del(request, rid):
    """
    删除角色
    :param request:
    :param rid:
    :return:
    """
    models.Role.objects.get(id=rid).delete()
    return redirect('role_list')