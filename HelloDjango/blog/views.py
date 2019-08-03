from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello_world(request) :
    # request 为封装好的请求参数
    return HttpResponse("Hello Django World!")

