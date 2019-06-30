from django.shortcuts import HttpResponse, render, redirect
from rbac import models
from rbac.service.init_permission import init_permissions

from django.conf import settings

def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        #   获取表单提交数据
        user = request.POST.get('user','')
        pwd = request.POST.get('pwd','')

        #   检验用户是否合法
        current_user = models.UserInfo.objects.filter(username=user,password=pwd).first()
        if not current_user:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})

        init_permissions(request, current_user)

        return redirect('/customer/list/')

