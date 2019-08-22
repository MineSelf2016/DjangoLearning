from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    context = dict()
    return render(request, "rumour/index.html", context)


def result(request):

    rumour_content = None
    rumour_prob = rumour_predict_label = rumour_true_label = None
    rumour_source = rumour_length = None
    rumour_publish_date = rumour_submit_date = None
    context = None

    try:
        rumour_content = request.POST["rumourContent"]
        rumour_source = request.POST["rumourSource"]
        rumour_length = request.POST["rumourLength"]
        rumour_publish_date = request.POST["rumourPublishDate"]
    except Exception as e:
        context = {
            "error_message" : "Please input necessary field"
        }
        return render(request, "rumour/index.html", context)
    

    if len(rumour_content) == 0:
        # 重新显示index.html 页面
        context = {
            "error_message" : "You didn't input rumour text."
        }
        return render(request, "rumour/index.html", context)
    else:
        rumour_prob = 0.987 * 100
        rumour_prob_str = "有较大可能性是谣言"
        context = {
            "rumour_content" : rumour_content,
            "rumour_prob" : rumour_prob,
            "rumour_prob_str" : rumour_prob_str
        }
        return render(request, "rumour/result.html", context)

    