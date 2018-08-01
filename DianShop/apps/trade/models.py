from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from goods.models import Goods
# Create your models here.

#返回类的实例对象
User = get_user_model()

#购物车
class ShopingCart(models.Model):
    user = models.ForeignKey(User,verbose_name="用户")
    goods = models.ForeignKey(Goods, verbose_name="商品")
    goods_nums = models.IntegerField(default=0, verbose_name="商品数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s(%s)".format(self.goods.name,self.goods_nums)

#订单
class OrderInfo(models.Model):
    ORDER_STATUS = (
        ("PAYING","待支付"),
        ("TRADE_SUCCESS", "支付成功"),
        ("TRADE_CLOSE", "关闭支付"),
        ("TRADE_FAIL", "支付失败"),
        ("TRADE_FINSHED", "交易结束"),
    )
    user = models.ForeignKey(User, verbose_name=u"用户")
    order_sn = models.CharField(max_length=30,unique=True, verbose_name="订单号")
    trade_sn = models.CharField(max_length=100,unique=True,blank=True,null=True, verbose_name="交易号")
    pay_status = models.CharField(default="PAYING",max_length=30,choices=ORDER_STATUS,verbose_name="订单状态")
    order_message = models.CharField(max_length=200,verbose_name="订单留言")
    order_amount = models.FloatField(default=0.0,verbose_name="订单金额")
    pay_time = models.DateTimeField(blank=True,null=True, verbose_name="支付时间")
    signing_name = models.CharField(max_length=30, verbose_name="签收人")
    signing_mobile = models.CharField(max_length=11,verbose_name="联系电话")
    address = models.CharField(max_length=200,verbose_name="收货地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


#订单商品详情
class OrderGoods(models.Model):
    #订单
    order = models.ForeignKey(OrderInfo,verbose_name="订单",related_name="goods",help_text="订单")
    #商品
    goods = models.ForeignKey(Goods, verbose_name="商品")
    #订单数量
    goods_nums = models.IntegerField(default=0, verbose_name="商品数量",help_text="商品数量")
    #添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")


    class Meta:
        verbose_name = "订单商品详情 "
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
