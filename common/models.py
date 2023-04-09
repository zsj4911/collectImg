from unicodedata import name
from django.db import models

# Create your models here.

class Task(models.Model):
    # 任务标题
    title = models.CharField(max_length=50)
    # 任务描述
    desc = models.CharField(max_length=200)
    # 文件存放路径
    filePath = models.CharField(max_length=100)
    # 文件内容
    fileContent = models.CharField(max_length=10)