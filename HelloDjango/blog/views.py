from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.core.paginator import Paginator

# Create your views here.


def hello_world(request) :
    # request 为封装好的请求参数
    return HttpResponse("Hello Django World!")


def index(request):
    cur_page = None
    previous_page = None
    next_page = None

    cur_page_str = request.GET.get("page")

    if cur_page_str:
        cur_page = int(cur_page_str)
    else:
        cur_page = 1

    
    print("cur_page param = ", cur_page)
    all_article_list = Article.objects.all()
    top5_article_list = Article.objects.order_by("-publish_date")[:6]
    pages = Paginator(all_article_list, 3)
    article_list = pages.page(cur_page).object_list

    page_num = pages.num_pages
    if cur_page == 1:
        previous_page = cur_page
        next_page = cur_page + 1
    elif cur_page == page_num:
        previous_page = cur_page - 1
        next_page = page_num
    else:
        previous_page = cur_page - 1
        next_page = cur_page + 1


    # print("pages num = ", page_num)
    # print("pages count = ", pages.count)
    # print("page1 = ", pages.page(1).object_list)

    context = {
        "article_list" : article_list,
        "top5_article_list" : top5_article_list,
        "page_num" : range(1, page_num + 1),
        "previous_page" : previous_page,
        "next_page" : next_page
    }
    return render(request, "blog/index.html", context)


def detail(request, blog_id):
    cur_article = previous_article = next_article = None
    # cur_article = Article.objects.get(article_id = blog_id)
    # previous_article = None
    # next_article = None

    articles = Article.objects.all()
    for index, article in enumerate(articles):
        if article.article_id == blog_id:
            cur_article = article
            try:
                previous_article = articles[index - 1]
            except Exception as e:
                previous_article = dict()
                previous_article["article_id"] = blog_id
                previous_article["title"] = "没有了-.-"
            try:
                next_article = articles[index + 1]
            except Exception as e:
                next_article = dict()
                next_article["article_id"] = blog_id
                next_article["title"] = "没有了-.-"
            break

    section_list = cur_article.content.split("\n")
    context = {
        "title" : cur_article.title,
        "section_list" : section_list,
        "previous_article" : previous_article,
        "next_article" : next_article
    }
    return render(request, "blog/detail.html", context)


def modify(request, blog_id):
    return HttpResponse("您正在访问第%s修改界面" % blog_id)




