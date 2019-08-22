from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pynlpir
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
        # rumour_content_split = pynlpir_segment(rumour_content, stopwords=stopwords)
        rumour_content_split = jieba_segment(rumour_content, stopwords=stopwords)
        print("rumour_content_split = ")
        print(rumour_content_split)
        vv = vect.transform(["异地 就医 结算"])
        rumour_prob = svm_clf.predict_proba(vv)[0][0]
        print("rumour_prob = ", rumour_prob)

        # rumour_prob = 0.987 * 100
        rumour_prob_str = "有较大可能性是谣言"
        context = {
            "rumour_content" : rumour_content,
            "rumour_prob" : rumour_prob,
            "rumour_prob_str" : rumour_prob_str
        }
        return render(request, "rumour/result.html", context)

    