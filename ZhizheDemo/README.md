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

