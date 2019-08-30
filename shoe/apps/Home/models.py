from django.db import models
from django.contrib.auth.models import AbstractUser
from easy_thumbnails.fields import ThumbnailerImageField
from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel

# 继承自AbstractUser
class User(AbstractUser):
    realname = models.CharField(max_length=8, verbose_name="真实姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    qq = models.CharField(max_length=11, verbose_name="QQ号")
    avator_sor = ThumbnailerImageField(upload_to="avator/%Y%m%d/", default="avator/default.jpg", verbose_name="头像")
class FindPassword(models.Model):
      verify_code = models.CharField(max_length=128, verbose_name="验证码")
      email = models.EmailField(verbose_name="邮箱")
      creat_time = models.DateTimeField(auto_now=True, verbose_name="重置时间")
      status = models.BooleanField(default=False, verbose_name="是否已重置")
class Address(BaseModel):
    """地址模型类"""
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='所属用户')
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收件地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    # 自定义一个模型管理器类
    # objects = AddressManager()

    class Meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
class AddressManager(models.Manager):
    """地址模型管理器类"""
    # 1. 改变原有查询的结果集:all()
    # 2. 封装方法:用户操作模型类对应的数据表(增删查改)

    def get_default_address(self, user):
        # 获取用户的默认收货地址
        try:
            address = self.get(user=user, is_default=True)
        except self.model.DoesNotExist:
            address = None  # 不存在默认地址

        return address