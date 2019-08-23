# DjangoLearning
Django学习记录

<hr>
8月23日：<br>
1、完成bootstrap studio 的下载与getting started；<br>
2、复习bootstrap，使用studio 临摹苹果与特斯拉官网；<br>
3、Azure 学生身份认证，挑选云服务器；<strong>Azure 学生认证失败！！我是大专生？？？</strong><br>
4、vscode <a href="https://code.visualstudio.com/docs/remote/remote-overview">remote</a>模块的使用，连接阿里云服务器，搭建nodeJS Demo；<br>
5、完善zhizhe 前端页面。<br>


Django 设置远程访问：
1. 在项目 setting.py 文件中注册host：
```python
ALLOWED_HOSTS = ["*"]
```

2. 设置启动项
```bash
nohup python3 manage.py runserver 0.0.0.0:8000 &
```
0.0.0.0 或本机ip 不能省略
