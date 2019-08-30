from django.contrib import admin

# Register your models here.
from .models import  GoodsType, IndexPromotionBanner, IndexGoodsBanner, IndexTypeGoodsBanner, Goods, GoodsSKU,GoodsImage
admin.site.register(Goods)
admin.site.register(IndexPromotionBanner)
admin.site.register(IndexGoodsBanner)
admin.site.register(IndexTypeGoodsBanner)
admin.site.register(GoodsSKU)
admin.site.register(GoodsType)
admin.site.register(GoodsImage)




