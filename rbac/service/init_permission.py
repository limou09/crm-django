from django.conf import settings

def init_permissions(request, current_user):
    """
    用户权限初始化
    :param current_user: 当前用户对象
    :param request: 请求相关所有数据
    :return:
    """
    #   获取用户信息和权限信息并消除重复值返回一个字典
    permission_queryset = current_user.roles.filter(permissions__url__isnull=False).values('permissions__id',
                                                                                           'permissions__url',
                                                                                           'permissions__name',
                                                                                           'permissions__title',
                                                                                           'permissions__parent_id',
                                                                                           'permissions__parent__name',
                                                                                           'permissions__menu_id',
                                                                                           'permissions__menu__title',
                                                                                           'permissions__menu__icon',
                                                                                           ).distinct()
    #   将查询结果存储至session
    request.session['user_info'] = {'id': current_user.id, 'name': current_user.username}

    menu_dict = {}  #   筛选出菜单和能成为子菜单的权限，用于显示菜单
    permission_dict = {} #  所有的权限,用于权限校验

    for row in permission_queryset:
        #   把每一条权限存放于列表中
        permission_dict[row['permissions__name']] = {
            'id':row['permissions__id'],
            'url': row['permissions__url'],
            'pid':row['permissions__parent_id'],
            'pname':row['permissions__parent__name'],
            'title':row['permissions__title']
        }

        #   获取当前的菜单id
        menu_id = row.get('permissions__menu_id')
        #   如果有菜单id说明是二级菜单记录，没有则跳过
        if not menu_id:
            continue

        #   如果菜单id不在menu_dict中说明是二级菜单（客户管理、信息管理），不在就是添加列表、修改列表。。等记录的子菜单
        if menu_id not in menu_dict:
            menu_dict[menu_id] = {
                'title': row['permissions__menu__title'],
                'icon' : row['permissions__menu__icon'],
                'children' : [
                    {'id':row['permissions__id'],'title' : row['permissions__title'], 'url' : row['permissions__url']}
                ]
            }
        else:
            menu_dict[menu_id]['children'].append({'id':row['permissions__id'],'title':row['permissions__title'],'url':row['permissions__url']})

    #   把权限信息和菜单信息存入session
    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
    request.session[settings.MENU_SESSION_KEY] = menu_dict