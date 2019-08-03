## 初始化项目
使用命令
```bash
django-admin startproject
```
完成项目的初始化工作，即构建一个Django项目；

使用命令
```bash
python3 manage.py startapp appName
```
完成一个Django应用的创建。

## Django应用 VS Django项目
* 每个应用可以管理自己的模型、视图、模板、路由和静态文件等；
* 一个Django项目包含一组配置和若干个Django应用。