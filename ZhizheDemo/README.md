# 智者项目演示系统
作者
<ul>
    <li>Qi Cong
    <li>Huang Zheying
</ul>

## 项目搭建
应用：rumour，包含首页index.html 与结果页result.html

### index.html
用于用户输入谣言文本，提交至Django 进行结果预测。
页面主体即为一个form 表单

### result.html
用于获得预测的谣言结果，结果值为(0, 1)，越接近1，则是谣言的可能性越大。

### 谣言数据model 设计
```html
<ol>
    <li class="text-info">谣言model 包含的字段</li>
    <li class="text-info">谣言内容</li>
    <li class="text-info">谣言来源</li>
    <li class="text-info">谣言长度</li>
    <li class="text-info">谣言发布时间</li>
    <li class="text-info">谣言预测提交时间</li>
    <li class="text-info">谣言预测概率</li>
    <li class="text-info">谣言预测类别</li>
    <li class="text-info">用户是否给予了反馈</li>
    <li class="text-info">谣言真实类别</li>
</ol>
```

### 部署ML 模型
按照NLP 流程完成模型的训练，
1、训练完成后，使用pickle 模块序列化vectorizer 与clf 对象至磁盘
```python
fw = open("ML_models/vect.pkl", "wb")
vect = pickle.dump(vectorizer, fw)
fw.close()

fw = open("ML_models/svm_clf_prob.pkl", "wb")
svm_clf = pickle.dump(clf, fw)
fw.close()
```

2、在rumour/views.py 文件中load 预训练完成的模型
```python
fr = open("rumour/ML_models/vect.pkl", "rb")
vect = pickle.load(fr)
fr.close()

fr = open("rumour/ML_models/svm_clf_prob.pkl", "rb")
svm_clf = pickle.load(fr)
fr.close()
```

3、使用模型
```python
    rumour_content = request.POST["rumourContent"]
    rumour_content_split = jieba.cut(rumour_content)
    
    vv = vect.transform(["异地 就医 结算"])
    rumour_prob = svm_clf.predict_proba(vv)[0]
```

完成 admin 端开发，可管理数据模型。

完善前端的展示界面，仍使用bootstrap。

