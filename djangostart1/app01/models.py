from django.db import models

# Create your models here.

# 定义一个表
# class 定义的一个类就是一个表
class UserInfo(models.Model):
    # 如果定义model的时候没有指定主键，
    # django自动添加一个名为id的字段作为主键

    username = models.CharField(max_length=18)
    # 一个属性就是一个字段
    email = models.EmailField()
    # 6-18
    password = models.CharField(max_length=128)
    nickname = models.CharField(max_length=32)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username