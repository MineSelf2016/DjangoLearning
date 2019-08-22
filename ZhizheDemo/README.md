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


下一步完成ML 模型的模块化导出，用于预测提交的文本，即 model.predict，重要步骤需记录。

注：关于Django restful api 的开发。

之后完成数据模型model 层的开发，完成数据持久化。

完成 admin 端开发，可管理数据模型。

完善前端的展示界面，仍使用bootstrap。

