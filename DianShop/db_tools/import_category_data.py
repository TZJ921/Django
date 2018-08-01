import os
import sys

# 独立使用models

# 得到当前文件的位置和名称
filename_path = os.path.realpath(__file__)
# C:\Users\Administrator\PycharmProjects\AtguiguShop\db_tools\import_category_data.py
print("filename_path==", filename_path)

# 只要得到目录名称
dirname = os.path.dirname(filename_path)
# C:\Users\Administrator\PycharmProjects\AtguiguShop\db_tools
print("dirname==", dirname)
sys.path.append(dirname + "../")
print(sys.path)

# 设置独立使用models--从manage.py拷贝过来的
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DianShop.settings")

# 导入django设置
import django

django.setup()

# 这行代码不能卸载前面，一定要写在django.setup()的后面
from goods.models import GoodsCategory, Goods, GoodsCategoryBrand, GoodsImage
from db_tools.data.category_data import row_data

for goods_detail in row_data:
    # print(goods_detail)
    goods = Goods()
    goods.name = goods_detail["name"]
    goods.market_price = float(goods_detail["market_price"].replace("￥", "").replace("元", ""))
    goods.shop_price = float(goods_detail["sale_price"].replace("￥", "").replace("元", ""))
    # 商品简单描述
    # 下面语法的含义是：如果goods_detail["desc"]不为None直接返回，否则返回”“
    goods.goods_brief = goods_detail["desc"] if goods_detail["desc"] is not None else ""
    # 商品富文本描述
    goods.goods_desc = goods_detail["goods_desc"] if goods_detail["desc"] is not None else ""
    # 商品封面取images的第一张图片
    # 如果没有就返回”“
    goods.goods_front_image = goods_detail["images"][0] if goods_detail["images"] is not None else ""

    # 商品输入什么类型
    # 取最后一个
    categorys_name = goods_detail["categorys"][-1]
    # 最好去查一下是否有这个类型
    categorys = GoodsCategory.objects.filter(name=categorys_name)
    if categorys:
        goods.category = categorys[0]
    # 保存goods
    goods.save()

    # 保存图片,一张图片放在一个GoodsImage对象里面
    for goods_image in goods_detail["images"]:
        goods_image_instace = GoodsImage()
        goods_image_instace.image = goods_image
        goods_image_instace.goods = goods
        # 保存图片
        goods_image_instace.save()
print(row_data)

all_GoodsCategory = GoodsCategory.objects.all()
print(all_GoodsCategory)
# 一级类目的数据
for level1_data in row_data:
    level1_instance = GoodsCategory()
    level1_instance.name = level1_data["name"]
    level1_instance.code = level1_data["code"]
    level1_instance.category_type = 1  # 类别属于一级类目
    # 保存数据
    level1_instance.save()
    # 二级类目的数据
    for level2_data in level1_data["sub_categorys"]:
        level2_instance = GoodsCategory()
        level2_instance.name = level2_data["name"]
        level2_instance.code = level2_data["code"]
        level2_instance.category_type = 2  # 类别属于二级类目
        # 这个不要忘记
        level2_instance.parent_category = level1_instance
        # 保存数据
        level2_instance.save()

        # 三级类目的数据
        for level3_data in level2_data["sub_categorys"]:
            level3_instance = GoodsCategory()
            level3_instance.name = level3_data["name"]
            level3_instance.code = level3_data["code"]
            level3_instance.category_type = 3  # 类别属于三级类目
            # 这个不要忘记
            level3_instance.parent_category = level2_instance
            # 保存数据
            level3_instance.save()
