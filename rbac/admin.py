from django.contrib import admin

from rbac import models
# Register your models here.


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    菜单admin
    """
    list_display =  ['title','icon']

@admin.register(models.Permission)
class PermissionAdmin(admin.ModelAdmin):
    """
    权限admin
    """
    list_display = ['title','url','menu','name']
    list_editable = ['url','name']

@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    """
    角色admin
    """
    list_display = ['title']

@admin.register(models.UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    """
    用户admin
    """
    list_display = ['username','email',]
