from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse
import re


class MiddlewareMixin(object):
    """
    因为django1.4x-1.9x没有MiddlewareMixin这个类，所以我们自己写一个就好
    """
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class RbacMiddlewares(MiddlewareMixin):
    """
    权限控制中间件
    """

    def process_request(self, request):
        """
        权限控制
        process_request:请求预处理 在django拿到请求后还没处理之前访问此函数
        :param request:
        :return:
        """
        #   获取当前请求的url
        current_url = request.path_info
        #   过滤白名单，如果在白名单就不做任何处理了
        for reg in settings.VALID_URL_LIST:
            if re.match(reg, current_url):
                return None

        #   获取当前用户所拥有的的所有权限
        permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)

        #   如果没有权限说明没有登录，则跳转登录
        if not permission_dict:
            return redirect('/login/')

        request.breadcrumb_list = [
            {'title':'首页', 'url':'/'}
        ]

        #   进行权限校验
        flag = False
        for item in permission_dict.values():
            id = item['id']
            pid = item['pid']
            pname = item['pname']
            reg = "^%s$" %item.get('url')
            #   判断当前用户是否有访问的此url的权限
            if re.match(reg, current_url):
                flag = True
                #   判断当前访问的url是否是菜单中的子菜单
                if pid:
                    request.current_menu_id = pid
                    request.breadcrumb_list.extend([
                        {'title':permission_dict[pname]['title'], 'url':permission_dict[pname]['url']},
                        {'title': item['title'], 'url': item['url']}
                    ])
                else:
                    request.current_menu_id = id
                    request.breadcrumb_list.extend([
                        {'title': item['title'], 'url': item['url']}
                    ])
                break

        #   没有访问权限
        if not flag:
            return HttpResponse("没有该权限")