from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello_world(request) :
    # request 为封装好的请求参数
    return HttpResponse("Hello Django World!")


def index(request):
    return HttpResponse("您正在浏览首页内容")


def content(request, blog_id):
    # blog_id 以URLConf 中的配置，从url 中截取出
    return HttpResponse("您正在浏览第%s详情内容" % blog_id)


def modify(request, blog_id):
    return HttpResponse("您正在访问第%s修改界面" % blog_id)




