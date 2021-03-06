#coding:utf-8
"""memberSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^member/', 'app.views.member'),
    url(r'^members/', 'app.views.listing'),
    url(r'^api/members', 'app.views.api_members'),
    url(r'^api/order', 'app.views.api_order'),
    url(r'^$', 'app.views.index'),
    url(r'^order$', 'app.views.order'),
    url(r'^orders/$', 'app.views.orders'),
    url(r'^api/items', 'app.views.items'),
    url(r'^api/item', 'app.views.item'),
]

admin.site.site_title = '管理后台'
admin.site.site_header = '管理后台'
admin.site.index_title = '首页'
