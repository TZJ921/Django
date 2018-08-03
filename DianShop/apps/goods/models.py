from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField


# Create your models here.

# 商品的类别
class GoodsCategory(models.Model):
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),

    )
    # 类名
    name = models.CharField(default="", max_length=30, verbose_name="类名", help_text="类别名")
    # 类目的编码
    code = models.CharField(default="", max_length=30, verbose_name="类别编码", help_text="类别编码")
    # 类目的描述
    desc = models.TextField(default="", verbose_name="类名描述", help_text="类名描述")
    # 类目的级别
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别", null=True,
                                        blank=True)
    # 父类目
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目", help_text="父类目",
                                        related_name="sub_cat")
    # 是否导航
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品的类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 商品的品牌
class GoodsCategoryBrand(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name="brands", verbose_name="商品类目", null=True, blank=True)
    name = models.CharField(max_length=30, verbose_name="品牌名字", help_text="品牌名字")
    desc = models.TextField(max_length=100, verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brand/images/")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品的品牌名"
        verbose_name_plural = verbose_name

        # 自定义表名
        db_table = "goods_goodsbrands"

    def __str__(self):
        return self.name


# 商品
class Goods(models.Model):
    category = models.ForeignKey(GoodsCategory, verbose_name="商品类目")
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品编号")
    name = models.CharField(max_length=100, verbose_name="商品名称")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.FloatField(default=0.0, verbose_name="市场价格")
    shop_price = models.FloatField(default=0.0, verbose_name="本店价格")
    goods_brief = models.TextField(max_length=500, verbose_name="商品简明描述")
    # 商品内容，富文本描述
    goods_desc = UEditorField(u'内容', width=1000, height=300, imagePath="goods/images/", filePath="goods/files/",
                              default="")
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    goods_front_image = models.ImageField(upload_to="goods/images/", verbose_name="封面图", null=True, blank=True)
    is_new = models.BooleanField(default=False, verbose_name="是否是新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 商品的图片
class GoodsImage(models.Model):
    goods = models.ForeignKey(Goods, verbose_name="商品轮播图", related_name="images")
    image = models.ImageField(upload_to="goods/goodsimages/", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


# 轮播的商品图片
class Banner(models.Model):
    goods = models.ForeignKey(Goods, verbose_name="商品")
    image = models.ImageField(upload_to='goods/banner', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
