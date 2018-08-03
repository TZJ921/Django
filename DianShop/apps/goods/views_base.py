from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from goods.models import Goods

#商品的列表页
class GoodsListView(View):
    #重写get方法
    def get(self,request):
        #得到商品的前十条数据
        # goods_list = Goods.objects.all()[:10]
        # #python里的列表
        # json_list = []
        # # print(goods_list)
        # for goods in goods_list:
        #     #字典
        #     json_item = {}
        #     #商品的名称
        #     json_item["name"] = goods.name
        #     #市场的价格
        #     json_item["market_price"] = goods.market_price
        #     #销售量
        #     json_item["sold_num"] = goods.sold_num
        #
        #     json_list.append(json_item)
        #
        # #把列表转化为字符串
        # from django.http import HttpResponse
        # import json
        #
        # # print(type(json_list))
        # content = json.dumps(json_list,ensure_ascii=False)
        # # print(type(content))
        # return HttpResponse(content,"application/json")


        #第二种方式返回商品列表
        goods_list = Goods.objects.all()[:10]
        #序列化，把内存中的对象转换为网络中能够传输的对象转换成python的对象
        from django.core import serializers
        import json
        data = serializers.serialize("json",goods_list)
        data = json.loads(data)
        return JsonResponse(data,safe=False)

        # response_data = serializers.serialize("json",goods_list)
        # print(type(response_data))
        # return HttpResponse(response_data, "application/json")