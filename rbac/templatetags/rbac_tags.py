from collections import OrderedDict
from django.template import Library
from django.conf import settings

import re

register = Library()

@register.inclusion_tag('rbac/menu.html')
def menu(request):
    """
    生成菜单
    :param request:
    :return:
    """
    #   获取session中的菜单字典
    menu_dict = request.session.get(settings.MENU_SESSION_KEY)
    #   把菜单字典做成有序字典
    ordered_dict = OrderedDict()

    for key in sorted(menu_dict):
        ordered_dict[key] = menu_dict[key]
        #   默认所有菜单为隐藏属性
        menu_dict[key]['class'] = 'hide'

        for node in menu_dict[key]['children']:
            #   激活菜单
            if request.current_menu_id == node['id']:
                node['class'] = 'active'
                menu_dict[key]['class'] = ''
    return {'menu_dict':ordered_dict}


@register.inclusion_tag('rbac/breadcrumb.html')
def breadcrumb(request):
    """
    导航条展示
    :param request:
    :return:
    """

    return {'breadcrumb_list':request.breadcrumb_list}


@register.filter
def has_permission(request, name):
    """

    :param request:
    :param name:
    :return:
    """
    permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
    # print(permission_dict,'-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    if name in permission_dict:
        print(name,'*/*/*/*/*/*/*/*/*/*/*/*')
        return True