import xadmin
from .models import Goods,GoodsCategory,GoodsCategoryBrand,GoodsImage,Banner



class GoodsAdmin(object):
   #根据字段控制显示
   list_display = ["name","click_num","sold_num","fav_num","goods_num","market_price",
               "shop_price","goods_desc","is_new","is_hot","add_time"]
   #添加搜索框，并且提供name搜索
   search_fields = ["name"]
   style_fields = {"goods_desc":"ueditor"}



class GoodsCategoryAdmin(object):
   list_display = ["name", "category_type", "parent_category", "add_time"]
   list_filter = ["category_type", "parent_category", "name"]
   search_fields = ['name', ]

class GoodsCategoryBrandAdmin(object):
   list_display = ["category", "image", "name", "desc"]

class GoodsImageAdmin(object):
   pass
class BannerAdmin(object):
   pass

#注册商品models
xadmin.site.register(Goods,GoodsAdmin)
xadmin.site.register(GoodsCategory,GoodsCategoryAdmin)
xadmin.site.register(GoodsCategoryBrand,GoodsCategoryBrandAdmin)
xadmin.site.register(GoodsImage,GoodsImageAdmin)
xadmin.site.register(Banner,BannerAdmin)