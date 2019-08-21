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
<b>模型层</b>

模型是真实数据的简单明确的描述。它包含了储存的数据所必要的字段和行为。用户只需要定义数据模型，然后其它的杂七杂八代码会自动从模型生成。

<b>数据库配置</b>
在使用ORM 之前，请先确保已正确配置第三方数据库。
在 projectName/settings.py 文件的DATABASES 字典中完成相关配置：
    ENGINE -- 可选值有：
    'django.db.backends.sqlite3'，'django.db.backends.postgresql'，'django.db.backends.mysql'，或 'django.db.backends.oracle'。其他<a href="https://docs.djangoproject.com/zh-hans/2.1/ref/databases/#third-party-notes">可用后端</a>。

    NAME -- 数据库的名称：
    如果使用的是 SQLite，数据库将是你电脑上的一个文件，在这种情况下， NAME 应该是此文件的绝对路径，包括文件名。默认值 os.path.join(BASE_DIR, 'db.sqlite3') 将会把数据库文件储存在项目的根目录。
如果你不使用 SQLite，则必须添加一些额外设置，比如<a href="https://docs.djangoproject.com/zh-hans/2.1/ref/settings/#std:setting-USER"> USER </a>、<a href="https://docs.djangoproject.com/zh-hans/2.1/ref/settings/#std:setting-PASSWORD"> PASSWORD </a>、<a href="https://docs.djangoproject.com/zh-hans/2.1/ref/settings/#std:setting-HOST"> HOST </a>等等。想了解更多数据库设置方面的内容，请看文档：<a href="https://docs.djangoproject.com/zh-hans/2.1/ref/settings/#std:setting-DATABASES"> DATABASES </a>。



<font color="gray">注：应用Django 完成ORM 时，需要确保以下几点的实现：

1、使用SQLite 以外的数据库，请确认在使用前已经<b>创建了数据库</b>；

2、使用SQLite 以外的数据库，确保向该用户提供 "create database" 权限；

3、在settings.py 文件中完成时区的设置，并要确保之后操作的所有时间均为UTC+8 ：
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


### Django shell 与 Django 数据库API
为什么需要Django shell：
1、临时性操作使用Django Shell 更加方便；

2、小范围Debug 更简单，不需要运行整个项目来测试；

方便开发，方便调试，方便debug。

输入命令
```
python3 manage.py shell
```
进入shell 交互模式

阅读 <a href="https://docs.djangoproject.com/zh-hans/2.1/ref/models/relations/">访问关系对象</a> 文档可以获取关于数据库关系的更多内容。想知道关于双下划线的更多用法，参见 <a href="https://docs.djangoproject.com/zh-hans/2.1/topics/db/queries/#field-lookups-intro">查找字段</a> 文档。数据库API的所有细节可以在 <a href="https://docs.djangoproject.com/zh-hans/2.1/topics/db/queries/">数据库 API 参考</a> 文档中找到。


### Django Admin 模块
Django Admin模块是Django 的后台管理工具，可以读取开发者定义的模型元数据，并提供强大的管理使用页面。

使用Admin 模块步骤：
    1. 创建管理员用户：
        1.1 命令 python3 manage.py createsuperuser;
        1.2 输入 username、email（可选）、password、password；
    2. 登录管理员页面：
        2.1 命令 python3 manage.py runserver;
        2.2 入口地址 127.0.0.1:8000/admin;

注册用户自定义模型：
在blog/admin.py 文件中，声明以下内容
```python
# Register your models here.
from .models import Article
admin.site.register(Article)
```

### Django 视图
在 Django 中，网页和其他内容都是从视图派生而来。每一个视图表现为一个简单的 Python 函数（或者说方法，如果是在基于类的视图里的话）。Django 将会根据用户请求的 URL 来选择使用哪个视图（更准确的说，是根据 URL 中域名之后的部分）。

#### 占位url
现在让我们向项目中添加更多视图，用来预先占位url。

1、编写视图函数，blog/views.py ：
```python
def index(request):
    return HttpResponse("您正在浏览首页内容")


def content(request, blog_id):
    # blog_id 以URLConf 中的配置，从url 中截取出
    return HttpResponse("您正在浏览第%s详情内容" % blog_id)


def modify(request, blog_id):
    return HttpResponse("您正在访问第%s修改界面" % blog_id)


```

2、注册应用级别路由，blog/urls.py：
```python
urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:blog_id>/content", views.content, name = "content"),
    path("<int:blog_id>/modify", views.modify, name = "modify"),
    path("hello_world", views.hello_world, name = "hello_world"),
]
```

3、注册项目级别路由，方法同上；

4、注册应用至项目，方法同上。


#### static页面开发
1、在blog/ 目录下新建目录 templates，在templates/下新建blog/ 目录，在blog/ 目录下新建index.html 文件；

2、在index.html 页面中使用bootstrap 编写静态页面；

3、浏览器中预览页面效果。


#### 模板系统
1、模板系统简介：
模板系统的表现形式为文本文件；
用于分离网页的内容与表现；
模板系统预定义了特有的标签占位符。

使用模板系统的原因：
    <ul>
        <li>views.py 文件不适合编码HTML；
        <li>页面设计的改变需要修改python 代码；
        <li>网页展示与网页逻辑应分开。
    </ul>


2、模板系统语法：
变量标签：
```python
    {{ 变量 }} ；
```

for 循环标签：
```python
<ul>
    {% for item in list %}
        <li> {{ item }}
    {% endfor %}
</ul>
```

if-else 分支标签：
```python
    {% if true %}
        <p>it's a true part.
    {% else %}
        <p>it's a false part.
    {% endif %}
```


3、模板系统用法：
3.1 在项目应用目录blog/ 下创建 templates 目录。Django 将会在这个目录里查找模板文件；<br>
3.2 在templates 目录下新建blog/ 目录，在blog/ 目录下新建index.html、detail.html ......文件；<br>
3.3 使用预定义标签编写模板文件，index.html：
```html
    <div class="col-md-9" role="main"> 
    {% for article in article_list %}
        <div class="h2">{{ article.title }}</div>
        <div class="p">{{ article.content }}</div>
    {% endfor %}
    </div>
```
3.4 在视图views.py 中完成数据的转发：
```python
def index(request):
    article_list = Article.objects.all()
    context = {
        "article_list" : article_list
    }
    return render(request, "blog/index.html", context)

"""
    The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. 
    It returns an HttpResponse object of the given template rendered with the given context.
"""
```


<small>注：在项目的 TEMPLATES 配置项中描述了 Django 如何载入和渲染模板。默认的设置文件设置了 DjangoTemplates 后端，并将 APP_DIRS 设置成了 True。这一选项将会让 DjangoTemplates 在每个 INSTALLED_APPS 文件夹中寻找 "templates" 子目录。</small>



