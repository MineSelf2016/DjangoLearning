## 初始化项目
使用命令
```bash
django-admin startproject projectName
```
完成项目的初始化工作，即构建一个Django项目；

使用命令
```bash
python3 manage.py startapp appName
```
完成一个Django应用的创建。

使用命令
```bash
python3 manage.py runserver 8000
```
完成服务器的启动，并监听8000 端口。

## Django项目 VS Django应用
* 项目是一个网站使用的配置和应用的集合；
* 应用是一个专门做某件事的网络应用程序；
* 每个应用可以管理自己的模型、视图、模板、路由和静态文件等；
* 一个项目可以包含很多个应用，一个应用可以被很多个项目使用。

## Django项目目录结构
* manage.py 一个让你用各种方式管理 Django 项目的命令行工具。你可以阅读<a href="https://docs.djangoproject.com/zh-hans/2.1/ref/django-admin/"> django-admin and manage.py </a>获取所有 manage.py 的细节。
* projectName/ 一个纯 Python 包。名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 projectName.urls).
* projectName/__init__.py 一个空文件，告诉 Python 这个目录应该被认为是一个<b> Python 包</b>。如果你是 Python 初学者，阅读官方文档中的<a href="https://docs.python.org/3/tutorial/modules.html#tut-packages">更多关于包的知识</a>。
* projectName/settings.py Django 项目的配置文件。如果你想知道这个文件是如何工作的，请查看<a href="https://docs.djangoproject.com/zh-hans/2.1/topics/settings/">Django settings</a>了解细节。
* projectName/urls.py Django 项目的 URL 声明，就像你网站的“目录”。阅读<a href="https://docs.djangoproject.com/zh-hans/2.1/topics/http/urls/">URL调度器</a>文档来获取更多关于 URL 的内容。
* projectName/wsgi.py 作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。阅读<a href="https://docs.djangoproject.com/zh-hans/2.1/howto/deployment/wsgi/">如何使用 WSGI 进行部署</a>了解更多细节。


## Django应用目录结构
* models.py 处理应用模型的文件；
* views.py 处理应用视图的文件；
* urls.py （自行创建）管理应用路由的地方；
* admin.py 定义Admin 模块管理对象的地方；
* app.py 声明应用的地方；
* tests.py 编写应用测试用例的地方。


## Django Hello World
在Django 中，每一个应用都是一个Python 包，并且遵循着相同的约定。


### Django 视图与Django 路由
1. 在blog/views.py 文件中创建hello_world 视图，使其做为Python 包导出
```python
from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request) :
    # request 为封装好的请求参数
    return HttpResponse("Hello Django world")
```


2. 应用层次路由配置：在blog/urls.py 文件中声明
```python
from django.urls import path, include
from . import views

urlpatterns = [
    path("hello_world", views.hello_world),
]
```
函数path() 具有四个参数，两个必须参数：route 和 view，两个可选参数：kwargs 和 name。


3. 项目层次路由配置：在HelloDjango/urls.py 的urlpatterns 列表里插入一个include()
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 函数 include() 允许引用其它 URLconfs。
    # 每当 Django 遇到 :func：~django.urls.include 时，
    # 它会截断与此项匹配的 URL 的部分，
    # 并将剩余的字符串发送到 URLconf 以供进一步处理。
    path("blog/", include("blog.urls")),
]
```


4. 注册blog app应用：在HelloDjango/settings.py 的INSTALLED_APPS 列表里加入用户自定义的应用
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 用户自定义app
    'blog.apps.BlogConfig',
]
```


### Django 模型层与Django 数据库
模型层

模型是真实数据的简单明确的描述。它包含了储存的数据所必要的字段和行为。用户只需要定义数据模型，然后其它的杂七杂八代码会自动从模型生成。

<font color="gray">注：应用Django 完成ORM 时，需要在settings.py 文件中完成时区的设置，并要确保之后操作的所有时间均为UTC+8 ：
```python
TIME_ZONE = 'Asia/Shanghai'

USE_TZ = True
```
</font>

完整创建一个model 需要以下两步（3步）：

* 编辑models.py 文件，创建（改变）model 类；
* 运行python3 manage.py makemigrations [应用名称] 为模型的创建（改变）生成迁移文件；
* 运行python3 manage.py migrate 应用数据库迁移。


1. 定义模型

    在blog/models.py 文件中加入以下内容创建模型：
    ```python
    # 1、设计模型结构（数据库字段）
    class Article(models.Model):
        # 1、设计模型结构；
        # 2、定义模型层字段类型
        articel_id = models.AutoField(primary_key = True)
        title = models.TextField()
        abstract = models.TextField()
        content = models.DateTimeField(auto_now = True)

    ```


2. 激活模型
 
    激活模型又称为数据库迁移，迁移是Django 对于模型定义（也就是你的数据库结构）的变化的储存形式，能让你在开发过程中持续的改变数据库结构而不需要重新删除和创建表。

    2.1 在HelloDjango/settings.py的的INSTALLED_APPS 列表里注册用户自定义应用：
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # 用户自定义app
        'blog.apps.BlogConfig',
    ]
    ```

    2.2 完成数据库迁移的生成
    ```bash
    python3 manage.py makemigrations [应用名称]
    ```
    通过运行 makemigrations 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次  migration。

    <font color="gray">注：
    
    使用sqlmigrate 命令查看SQL 语句：
    ```bash
    python3 manage.py sqlmigrate [应用名称] 0001
    ```
    使用check 命令检查项目中的问题：
    ```bash
     python3 manage.py check 
    ```
    </font>

    2.3 完成数据库迁移的应用
    ```bash
    python3 manage.py migrate
    ```
    migrate 命令选中所有还没有执行过的迁移，并应用在数据库上，也就是将你对模型的更改同步到数据库结构上。





