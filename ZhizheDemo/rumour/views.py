from django.shortcuts import render
from django.http import HttpResponse
from .models import Rumour
from django.http import JsonResponse
import pickle
import jieba

fr = open("rumour/ML_models/vect.pkl", "rb")
vect = pickle.load(fr)
fr.close()

fr = open("rumour/ML_models/svm_clf_prob.pkl", "rb")
svm_clf = pickle.load(fr)
fr.close()

StopwordsFilename_1 ="rumour/ML_models/stopwords.txt"
stopwords = []
# 生成基本停用词列表
for line in open(StopwordsFilename_1,encoding='utf8').readlines():
    stopwords.append(line.strip())# .strip()去掉换行符

# 自定义分词函数
def jieba_segment(content, stopwords):
    seg_list = jieba.cut(content)
    removed_seg_list = []
    ##过滤停用词
    for w in seg_list:
        if w not in stopwords:
            removed_seg_list.append(w)
    return " ".join(removed_seg_list) # 返回每一条谣言分词的字符串


# Create your views here.
def index(request):
    context = dict()
    return render(request, "rumour/index.html", context)


def result(request):
    rumour = Rumour()
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

        rumour.rumour_content = rumour_content

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
        rumour_content_split = jieba_segment(rumour_content, stopwords=stopwords)
        vv = vect.transform([rumour_content_split])

        # rumour_prob 取值范围 (0, 1)
        rumour_prob = svm_clf.predict_proba(vv)[0][0]

        rumour.rumour_predicted_label = 1
        rumour.rumour_true_label = 1
        rumour.rumour_prediced_prob = rumour_prob
        rumour.save()

        rumour_prob_str = "有较大可能性是谣言"
        context = {
            "rumour_id" : rumour.rumour_id,
            "rumour_content" : rumour_content,
            "rumour_prob" : rumour_prob,
            "rumour_prob_str" : rumour_prob_str
        }
        return render(request, "rumour/result.html", context)

    
def feedback(request):
    # 完成ajax 请求数据的返回
    # 前端发送参数comment，为1 时，预测正确，为0 时，预测错误
    comment_str = comment = predicted_prob_str = predicted_prob = rumour_id_str = rumour_id = None
    context = None
    try:
        rumour_id_str = request.POST["rumour_id"]
        comment_str = request.POST["comment"]
        predicted_prob_str = request.POST["rumour_prob"]
    except Exception as e:
        context = {"errorMsg": "illegal post, there is some params lacked"}
        return JsonResponse(context)
    rumour_id = int(rumour_id_str)
    comment = int(comment_str)
    predicted_prob = float(predicted_prob_str)
    print("rumour_id = ", rumour_id)
    print("comment = ", comment)
    print("predicted_prob = ", predicted_prob)
    rumour = Rumour.objects.get(rumour_id = rumour_id)
    if comment == 1:
        rumour.rumour_true_label = (1 if (predicted_prob >= 0.5) else 0)
    else:
        rumour.rumour_true_label = (0 if (predicted_prob >= 0.5) else 1)
    print("rumour = ", rumour)
    rumour.save()
    context = {"flag": 1}
    return JsonResponse(context)