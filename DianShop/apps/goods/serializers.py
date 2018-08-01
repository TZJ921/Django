from django.views.generic import View
from django.core import serializers
from django.http import JsonResponse
from rest_framework import serializers
from .models import Goods,GoodsCategory
import json


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsListView(View):
    def get(self,request):
        goods_list = Goods.objects.all()[:10]

        data = serializers.serialize("json", goods_list)
        data = json.loads(data)

        return JsonResponse(data, safe=False)

class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)
    category = GoodsCategorySerializer()

    name = serializers.CharField(max_length=100)
    click_num = serializers.IntegerField(default=0)
    sold_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.ImageField(default="")

    class Meta:
        model = Goods

        #fields = ('name','click_num','sold_num','goods_fron_image','add_time')
        fields = "__all__"

