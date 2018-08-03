from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#重写user，继承数据库
class UserProfile(AbstractUser):
    #姓名help_text，自动生成文档时用
    name = models.CharField(max_length=30,null=True,blank=True,verbose_name="姓名",help_text="姓名")
   #生日
    birthday = models.DateField(null=True,blank=True,verbose_name="出生年月")
   #性别
    gender = models.CharField(max_length=6,choices=(("male","男"),("female","女")),default="female",verbose_name="性别")
    #手机号
    mobile = models.CharField(max_length=11,verbose_name="电话号码")
    #电子邮件
    email = models.EmailField(max_length=30,null=True,blank=True,verbose_name="电子邮件",help_text="电子邮件")

    class Meta:
        verbose_name = "用户"
        #在admin中，用户信息中没有s
        verbose_name_plural = verbose_name

    def __str__(self):
        #返回该对象的信息
        return self.username

#短信验证码
class VerifyCode(models.Model):
    #验证码
    code = models.CharField(max_length=6, verbose_name="验证码",help_text="验证码")
    #手机号
    mobile = models.CharField(max_length=11, verbose_name="电话号码")
   #添加时间（校验刚才有没有注册）
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = "短信验证码"

    def __str__(self):
        return self.code
