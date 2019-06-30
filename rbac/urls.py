from django.conf.urls import url

from rbac.views import role
from rbac.views import menu

urlpatterns = [
    # 角色列表
    url(r'^role/list/$', role.role_list, name='role_list'),
    #  角色添加
    url(r'^role/add/$', role.role_add, name='role_add'),
    #   角色修改
    url(r'^role/edit/(?P<rid>\d+)/$', role.role_edit, name='role_edit'),
    #   角色删除
    url(r'^role/del/(?P<rid>\d+)/$', role.role_del, name='role_del'),

    #   菜单列表
    url(r'^menu/list/$', menu.menu_list, name='menu_list'),
    #   添加菜单
    url(r'^menu/add/$', menu.menu_add, name='menu_add'),
    #  修改菜单
    url(r'^menu/edit/(?P<mid>\d+)/$', menu.menu_edit, name='menu_edit'),
    #   删除菜单
    url(r'^menu/del/(?P<mid>\d+)/$', menu.menu_del, name='menu_del'),

]