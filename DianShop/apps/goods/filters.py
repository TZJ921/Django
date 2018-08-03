from django_filters import rest_framework as filters
from .models import Goods


#商品的过滤器
class GoodsFilter(filters.FilterSet):
    #最低价格
    min_price = filters.NumberFilter(field_name="shop_price",lookup_expr='gte')
    #最高价格
    max_price = filters.NumberFilter(field_name="shop_price",lookup_expr='lte')

    #针对商品的名字进行模糊查询
    name = filters.CharFilter(field_name="name",lookup_expr='icontains')
    goods_brief = filters.CharFilter(field_name="goods_brief",lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['min_price','max_price']