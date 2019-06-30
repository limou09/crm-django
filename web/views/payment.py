from django.shortcuts import render,redirect

from web import models
from web.forms.payment import PaymentForm, PaymentUserForm


def payment_list(request):
    """
    付费账单列表
    :param request:
    :return:
    """
    data_list = models.Payment.objects.all()
    return render(request, 'payment_list.html',{'data_list': data_list})


def payment_add(request):
    """
    添加付费记录
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = PaymentForm()
        return render(request, 'payment_add.html', {'form':form})

    form = PaymentForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/payment/list/')
    return render(request,'payment_add.html',{'form':form})


def payment_edit(request, pid):
    """
    修改付费记录
    :param request:
    :return:
    """
    try:
        obj = models.Payment.objects.get(id=pid)
    except Exception as e:
        print("修改付费记录找不到信息：", e)

    if request.method == 'GET':
        form = PaymentForm(instance=obj)
        return render(request, 'payment_edit.html', {'form':form})

    if request.method == 'POST':
        form = PaymentForm(data=request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/payment/list/')
        return render(request, 'payment_edit.html', {'form':form})


def payment_del(request, pid):
    """
    删除付费记录
    :param request:
    :param pid:
    :return:
    """
    models.Payment.objects.get(id=pid).delete()
    return redirect('/payment/list/')