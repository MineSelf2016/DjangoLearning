from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    context = dict()
    return render(request, "rumour/index.html", context)


def result(request):

    context = dict()
    return render(request, "rumour/result.html", context)

    