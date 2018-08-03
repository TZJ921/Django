from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Goods,GoodsCategory
from .serializers import GoodsSerializer
from rest_framework.views import APIView
#自己封装了response
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers,mixins,generics,viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
# Create your views here.

#只显示被序列的数据
class GoodsListView(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # def get(self,request,format=None):
    #     goods = Goods.objects.all()[:10]
    #     goods_serializer = GoodsSerializer(goods,many=True)
    #     return Response(data=goods_serializer.data)

#分页
class GoodsListPagination(PageNumberPagination):
    page_size = 4
#     #使用默认字段
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100

#进行分页显示
class GoodsListAPIView(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsListPagination


#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.CreateModelMixin):

class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    # 得到所有的商品
    queryset = Goods.objects.all()
    # 序列化器
    serializer_class = GoodsSerializer
    # 添加分页配置,settings.py就可以省略了
    pagination_class = GoodsListPagination

    filter_class = GoodsFilter
    # 支持搜索和过滤，写在一起
    filter_backends = (filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend)
    search_fields = ('^name','goods_brief','goods_desc')
    # 过滤的字段
    # filter_fields = ('name','shop_price')
    ordering_fields = ('shop_price','add_time')


    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #
    #     min_price = self.request.query_params.get("min_price",0)

    #     if min_price:
    #          #得到价格过滤
    #         queryset = queryset.filter(shop_price__gte=int(min_price))
    #
    #     return queryset

    #     价格大于100的
    #     return self.queryset.filter(shop_price__gte=100)

#
#     def get(self,request,format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods,many = True)
#         return Response(data=goods_serializer.data)

#商品类别
# class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
#     queryset = GoodsCategory.objects.filter(category_type=1)
#     serializer_class = CategorySerializer

#返回商品列表

class GoodsSerialize(serializers.Serializer):
    name = serializers.CharField(max_length=100)
#     # 点击数
    click_num = serializers.IntegerField(default=0)
#     # 销售量
    sold_num = serializers.IntegerField(default=0)
#     # 封面，自动帮我在图片的路径前面加上media
    goods_front_image = serializers.ImageField(default="")



