from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.


def hello_world(request) :
    # request 为封装好的请求参数
    return HttpResponse("Hello Django World!")


def index(request):
    article_list = Article.objects.all()
    context = {
        "article_list" : article_list
    }
    return render(request, "blog/index.html", context)


def detail(request, blog_id):
    # blog_id 以URLConf 中的配置，从url 中截取出
    article = Article.objects.get(article_id = blog_id)
    section_list = article.content.split("\n")
    context = {
        "title" : article.title,
        "section_list" : section_list
    }
    return render(request, "blog/detail.html", context)


def modify(request, blog_id):
    return HttpResponse("您正在访问第%s修改界面" % blog_id)




