import xadmin
from .models import VerifyCode
from xadmin import views


class GlobalSettings(object):
    #配置标题
    site_title = "甜甜商店后台"
    #底部配置
    site_footer = "tiantian_shop"


class VerifyCodeAdmin(object):
     # 字段控制展示显示
    list_display = ['code','mobile','add_time']

# 注册
xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.CommAdminView,GlobalSettings)
