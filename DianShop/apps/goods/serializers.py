from django.views.generic import View
from django.core import serializers
from django.http import JsonResponse
from rest_framework import serializers
from goods.models import Goods,GoodsCategory
import json


# class CategorySerializer3(serializers.ModelSerializer):
#     class Meta:
#         model = GoodsCategory
#         fields = "__all__"

# class CategorySerializer2(serializers.ModelSerializer):
#     sub_cat = CategorySerializer3(many=True)
#     class Meta:
#         model = GoodsCategory
#         fields = "__all__"

# class CategorySerializer(serializers.ModelSerializer):
#     sub_cat = CategorySerializer2(many=True)
#     class Meta:
#         model = GoodsCategory
#         fields = "__all__"

#商品类型序列化
class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

#Model基本的序列化，每一个字段不需要自己写,使用rest_framework 序列化
class GoodsSerializer(serializers.ModelSerializer):
#     # sub_cat = CategorySerializer2(many=True)
#     # category = GoodsCategorySerializer()
#     #适合自定义
#     # class GoodsSerializer(serializers.ModelSerializer):
#     # name = serializers.CharField(max_length=100)
#     # click_num = serializers.IntegerField(default=0)
#     # sold_num = serializers.IntegerField(default=0)
#     # goods_front_image = serializers.ImageField(default="")
#
    class Meta:
#         #指定序列化的model
        model = Goods
#         #显示个别用此方法
#         #fields = ('name','click_num','sold_num','goods_fron_image','add_time')
#         #要序列化的子段
        fields = "__all__"


