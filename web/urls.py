from django.conf.urls import url

from web.views import account
from web.views import customer
from web.views import payment

urlpatterns = [
    # 客户列表
    url(r'^customer/list/$', customer.customer_list, name='customer_list'),
    # 添加客户
    url(r'^customer/add/$', customer.customer_add, name='customer_add'),
    # 修改客户
    url(r'^customer/edit/(?P<cid>\d+)/$', customer.customer_edit, name='customer_edit'),
    #  删除客户
    url(r'^customer/del/(?P<cid>\d+)/$', customer.customer_del, name='customer_del'),
    # 批量导入
    url(r'^customer/import/$', customer.customer_import, name='customer_import'),
    #  批量下载
    url(r'^customer/tpl/$', customer.customer_tpl, name='customer_tpl'),

    #   付费记录列表
    url(r'^payment/list/$', payment.payment_list, name='payment_list'),
    #   添加付费记录
    url(r'^payment/add/$', payment.payment_add, name='payment_add'),
    #   修改付费记录
    url(r'^payment/edit/(?P<pid>\d+)/$', payment.payment_edit, name='payment_edit'),
    #  删除付费记录
    url(r'^payment/del/(?P<pid>\d+)/$', payment.payment_del, name='payment_del'),

    #   登录
    url(r'^login/$', account.login),

]