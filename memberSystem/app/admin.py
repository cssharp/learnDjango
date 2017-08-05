from django.contrib import admin
from models import Member, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('mobile', 'userName', 'createTime', 'isReceiveOrder')
    search_fields = ('mobile', 'userName')
    list_filter = ('isReceiveOrder', 'isPurchased', 'isConfirmReceipt')
    list_per_page = 10


# Register your models here.
admin.site.register(Member)
admin.site.register(Order, OrderAdmin)

