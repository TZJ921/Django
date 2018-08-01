from django.conf.urls import url,include
from django.views.static import serve
import xadmin
from goods.views import *
from DianShop.settings import MEDIA_ROOT
from goods.views_base import GoodsListView

urlpattern = [
   # url(r'^xadmin/',xadmin.site.urls),
    #url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    url(r'^goods/$',GoodsListView.as_view(),name="goods_list")

]