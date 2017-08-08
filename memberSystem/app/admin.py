#coding:utf-8

from django.contrib import admin
from models import Member, Order, Item


class OrderAdmin(admin.ModelAdmin):
    list_display = ('mobile', 'userName', 'createTime', 'isReceiveOrder')
    search_fields = ('mobile', 'userName')
    list_filter = ('isReceiveOrder', 'isPurchased', 'isConfirmReceipt')
    list_per_page = 10
    list_editable = ['isReceiveOrder', 'userName']


class ItemAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return u'<img src="%s" weight=10 height=10/>' % obj.itemPic1.url
    image_tag.short_description = '主图'
    image_tag.allow_tags = True
    list_display = ('image_tag', 'itemId', 'itemWeight', 'itemName', 'itemUSDPrice', 'itemCnPrice')

# Register your models here.
admin.site.register(Member)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)
