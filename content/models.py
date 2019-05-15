from django.db import models


# Create your models here.
class Article(models.Model):
    article_id = models.TextField("主键pk", primary_key=True)
    title = models.TextField("文章标题", max_length=50)
    brief_content = models.TextField("文章摘要", max_length=500)
    article_content = models.TextField("文章内容", max_length=10000)
    create_time = models.DateTimeField("创建时间", auto_now=True)

    # admin的数据显示
    def __str__(self):
        return self.title
