from django.db import models
from .validator import valid_difficulty
from ckeditor.fields import RichTextField
# 含文件上传
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    name = models.CharField("分类名称",max_length=64)
    class Meta:
        verbose_name = "分类"
        verbose_name_plural=verbose_name
    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    """标签"""
    name = models.CharField("标签名", max_length=64)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"
class Shop(models.Model):
    DIF_CHOICES = (
    (1, "男性"),
    (2, "价格"),
    (3, "女性"),
    (4, "颜色"),
    (5, "大小"),
    )
    shoes = models.IntegerField("商品分类",choices=DIF_CHOICES,validators=[valid_difficulty],null=True)
    category = models.ForeignKey(Category, verbose_name="所属分类", null=True)
    image = models.ImageField(upload_to='shoes', verbose_name='商品图片')
    title = models.CharField("商品名字", unique=True, max_length=256,null=True)
    price = models.CharField("商品价格", unique=True, max_length=256,null=True)
    content = RichTextUploadingField("商品详情", null=True)
    pub_time = models.DateTimeField("入库时间", auto_now_add=True, null=True)
    status = models.BooleanField("审核状态", default=False)
    tag = models.ManyToManyField(Tag, verbose_name="商品标签")
    class Meta:
        verbose_name="鞋库"
        verbose_name_plural= verbose_name

    def __str__(self):
            return f"{self.id}:{self.title}"

# from apps.Home.models import User
# class ShoesCollection(models.Model):
#     """收藏问题"""
#     pingpai= models.ForeignKey(Shop, verbose_name="名字", related_name='shoes_collection_set')
#     user = models.ForeignKey(User, verbose_name="收藏者", related_name='shoes_collection_set')
#     create_time = models.DateTimeField("收藏/取消时间", auto_now=True)
#     # True表示收藏 ,False表示未收藏
#     status = models.BooleanField("收藏状态", default=True)
#
#     class Meta:
#         verbose_name = "收藏记录"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         if self.status:
#             ret = "收藏"
#         else:
#             ret = "取消收藏"
#         return f"{self.user}:{ret}:{self.question.title}"

# from django.db import models
#
# # Create your models here.
#
#
# class TypeInfo(models.Model):
#     type_title = models.CharField('类型名称', max_length=20)
#     is_delete = models.BooleanField('是否删除', default=False)
#
#     def __str__(self):
#         return self.type_title
#
#     class Meta:
#         verbose_name = '分类信息'
#         verbose_name_plural = '分类信息'
#
# class GoodsInfo(models.Model):
#     goods_title = models.CharField('商品名称', max_length=20)
#     goods_name = models.CharField('商品简称', max_length=20, null=True, blank=True)
#     goods_pic = models.ImageField('商品图片', upload_to='df_goods', null=True, blank=True)  # 商品图片
#     goods_price = models.DecimalField('商品价格', max_digits=7, decimal_places=2)  # 总共最多有7位,小数占2位
#     goods_unit = models.CharField('商品单位', max_length=20, default='500g')  # 商品的单位
#     goods_click = models.IntegerField('点击量')  # 商品点击量,便于排人气
#     is_Delete = models.BooleanField('是否删除', default=False)
#     goods_jianjie = models.CharField('简介', max_length=200)  # 商品简介
#     goods_kucun = models.IntegerField('库存')  # 商品库存
#
#     goods_type = models.ForeignKey(TypeInfo, verbose_name='所属分类', on_delete=models.CASCADE)  # 商品所属类型
#
#
#     # gadv = models.BooleanField(default=False)   #商品推荐
#     class Meta:
#         verbose_name = '商品信息'
#         verbose_name_plural = '商品信息'


