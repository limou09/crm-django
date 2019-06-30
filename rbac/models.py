from django.db import models

# Create your models here.


class Menu(models.Model):
    """
    菜单
    """
    title = models.CharField(verbose_name='菜单名称', max_length=32, unique=True)
    icon = models.CharField(verbose_name='图标', max_length=32)

    def __str__(self):
        return self.title

class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的URL', max_length=128)
    name = models.CharField(verbose_name='URL的别名', max_length=32, unique=True)
    parent = models.ForeignKey(verbose_name='父权限', to='Permission', null=True, blank=True)
    menu = models.ForeignKey(verbose_name='菜单', to='Menu', blank=True, null=True, help_text='null表示非菜单')

    def __str__(self):
        return self.title

class Role(models.Model):
    """
    角色表
    """
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有的权限', to='Permission', blank=True)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """
    用户信息表
    """
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='邮箱', max_length=32)
    roles = models.ManyToManyField(verbose_name='拥有的角色', to='Role', blank=True)

    def __str__(self):
        return self.username