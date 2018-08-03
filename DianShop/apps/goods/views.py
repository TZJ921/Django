from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Goods,GoodsCategory
from .serializers import GoodsSerializer
from rest_framework.views import APIView
#自己封装了response
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers,mixins,generics,viewsets
from rest_framework import serializers

# Create your views here.

class GoodsListView(APIView):
    def get(self,request,format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods,many=True)
        return Response(data=goods_serializer.data)

# class GoodsListPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     page_query_param = "p"
#     max_page_size = 100


# class GoodsListAPIView(mixins.ListModelMixin,generics.GenericAPIView,generics.ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     # pagination_class = GoodsListPagination
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#商品类别
# class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
#     queryset = GoodsCategory.objects.filter(category_type=1)
#     serializer_class = CategorySerializer

#返回商品列表
# class GoodsListViewSet(mixins.ListModelMixin,generics.GenericAPIView,viewsets.GenericViewSet):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsListPagination
#
#     def get(self,request,format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods,many = True)
#         return Response(data=goods_serializer.data)

class GoodsSerialize(serializers.Serializer):
    name = serializers.CharField(max_length=100)
#     # 点击数
    click_num = serializers.IntegerField(default=0)
#     # 销售量
    sold_num = serializers.IntegerField(default=0)
#     # 封面，自动帮我在图片的路径前面加上media
    goods_front_image = serializers.ImageField(default="")



