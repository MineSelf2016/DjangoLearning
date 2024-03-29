from django.db import models

# Create your models here.

class Article(models.Model):
    # 1、设计模型结构；
    # 2、定义模型层字段类型
    article_id = models.AutoField(primary_key = True)
    title = models.TextField()
    brief_content = models.TextField()
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        # admin 页面展示时的字段内容
        return self.title