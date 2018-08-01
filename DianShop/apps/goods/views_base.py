from django.views.generic import View
from goods.models import Goods

#商品的列表页
class GoodsListView(View):
    def get(self,request):
        goods_list = Goods.objects.all()[:10]
        json_list = []
        print(goods_list)
        for goods in goods_list:
            json_item = {}
            json_item["name"] = goods.name
            json_item["market_price"] = goods.market_price
            json_item["sold_num"] = goods.sold_num

            json_list.append(json_item)

        from django.http import HttpResponse
        import json

        print(type(json_list))
        content = json.dumps(json_list)
        print(type(content))
        return HttpResponse(content,"application/json")