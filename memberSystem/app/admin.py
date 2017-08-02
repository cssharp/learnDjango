from django.contrib import admin
from models import Member, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('mobile', 'userName', 'createTime', 'isReceiveOrder')
    search_fields = ('mobile', 'userName')

# Register your models here.
admin.site.register(Member)
admin.site.register(Order, OrderAdmin)

