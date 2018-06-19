from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.


# 用户
class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField("电话", max_length=45)
    address = models.CharField("地址", max_length=45, null=True)
    country = models.CharField("国家", max_length=10, null=True)



# 分类
class Category(models.Model):

    name = models.CharField("分类名", max_length=45)


# 商品
class Product(models.Model):

    name = models.CharField("商品名", max_length=45)
    price = models.FloatField("价格")
    description = models.TextField("描述", max_length=300)
    last_update = models.DateTimeField("更新日期", auto_now=True)
    category = models.ForeignKey(Category, verbose_name="分类", on_delete=models.CASCADE)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'last_update')



# 订单
class CustomerOrder(models.Model):

    amount = models.FloatField("总价")
    date_create = models.DateTimeField("创建时间", auto_now=True)
    submitted = models.BooleanField("是否提交")
    customer = models.ForeignKey(Customer, verbose_name="客户", on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, verbose_name="商品", through='OrderProduct',
                                     through_fields=('customerorder', 'product'))

class CustomerOrderAdmin(models.Model):
    list_display = ('product', 'datecreate')

class OrderProduct(models.Model):

    customerorder = models.ForeignKey("CustomerOrder", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
