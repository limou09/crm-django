# crm-django

CRM，客户关系管理系统（Customer Relationship Management）。企业用CRM技术来管理与客户之间的关系，以求提升企业成功的管理方式，其目的是协助企业管理销售循环：新客户的招徕、保留旧客户、提供客户服务及进一步提升企业和客户的关系，并运用市场营销工具，提供创新式的个人化的客户商谈和服务，辅以相应的信息系统或信息技术如数据挖掘和数据库营销来协调所有公司与顾客间在销售、营销以及服务上的交互。


环境依赖：<br>
  django 1.9.1<br>
  python 3.6<br>
  
  
简单使用：<br>
  目前系统还存在一些bug，还在持续维护中。<br>
  python manage.py runserver<br>
  url:http://127.0.0.1:8000/login/<br>
  username:lidanyang password:lidanyang<br>


项目结构：<br>
├─Permission_RBAC 项目目录<br>
├─rbac  权限控制<br>
│  ├─forms  表单目录<br>
│  ├─middlewares  自定义中间件<br>
│  ├─migrations 迁移文件目录<br>
│  ├─service  <br>
│  ├─static 静态文件<br>
│  ├─templates  模板文件<br>
│  ├─templatetags 模板函数<br>
│  ├─views  视图<br>
└─web 业务逻辑<br>
    ├─files 文件<br>
    ├─forms 表单<br>
    ├─migrations 迁移文件<br>
    ├─static  静态文件<br>
    ├─templates 模板文件<br>
    ├─views 视图<br>

项目截图：<br>
  ![image](https://github.com/limou09/crm-django/blob/master/1.png)<br>
  ![image](https://github.com/limou09/crm-django/blob/master/2.png)<br>
