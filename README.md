# crm-django

CRM，客户关系管理系统（Customer Relationship Management）。企业用CRM技术来管理与客户之间的关系，以求提升企业成功的管理方式，其目的是协助企业管理销售循环：新客户的招徕、保留旧客户、提供客户服务及进一步提升企业和客户的关系，并运用市场营销工具，提供创新式的个人化的客户商谈和服务，辅以相应的信息系统或信息技术如数据挖掘和数据库营销来协调所有公司与顾客间在销售、营销以及服务上的交互。


环境依赖：
  django 1.9.1
  python 3.6
  
  
简单使用：
  目前系统还存在一些bug，还在持续维护中。
  python manage.py runserver
  url:http://127.0.0.1:8000/login/
  username:lidanyang password:lidanyang


项目结构：
├─Permission_RBAC 项目目录
├─rbac  权限控制
│  ├─forms  表单目录
│  ├─middlewares  自定义中间件
│  ├─migrations 迁移文件目录
│  ├─service  
│  ├─static 静态文件
│  ├─templates  模板文件
│  ├─templatetags 模板函数
│  ├─views  视图
└─web 业务逻辑
    ├─files 文件
    ├─forms 表单
    ├─migrations 迁移文件
    ├─static  静态文件
    ├─templates 模板文件
    ├─views 视图

项目截图：
  
