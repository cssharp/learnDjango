#coding:utf-8
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Member, Order
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
import json


def index(req):
    return render_to_response('bootstrap.html',)

# Create your views here.
def member(request):
    members = Member.objects.all()
    return render(request, 'index.html', {'members':members})


def listing(request):
    member_list = Member.objects.all()
    paginator = Paginator(member_list, 2) # Show 2 members per page

    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        members = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        members = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'members': members})


def api_members(request):
    members = Member.objects.all()
    jsonStrx = serializers.serialize('json', members)

    j = json.loads(jsonStrx)
    jsonStrx = json.dumps(j, indent=4)

    return HttpResponse(jsonStrx, content_type="application/json")


def api_order(request):
    if request.method == 'POST':
        url = request.POST.get('url', "")
        mobile = request.POST.get('mobile', "")
        userName = request.POST.get('userName', "")
        price = request.POST.get('price', None)
        if not price.isdigit():
            price = None

        desc = request.POST.get('desc', "")

        if(mobile==''):
                return HttpResponse(u'{"result":-1, "desc":"手机号无效"}', content_type="application/json")
        orderId = Order.objects.create(userName=userName, url=url, mobile=mobile, desc=desc, price=price)
        return HttpResponse(u'{"result":0, "desc":"successful"}', content_type="application/json")
    return HttpResponse(u'{"result":-99, "desc":"无效请求"}', content_type="application/json")


def order(request):
    if request.method == 'POST':
        url = request.POST.get('url', "")
        mobile = request.POST.get('mobile', "")
        userName = request.POST.get('userName', "")
        price = request.POST.get('price', None)
        if not price.isdigit():
            price = None

        desc = request.POST.get('desc', "")

        if(mobile==''):
             return HttpResponse(u'{"result":-1, "desc":"手机号无效"}', content_type="application/json")
        orderId = Order.objects.create(userName=userName, url=url, mobile=mobile, desc=desc, price=price)
        return HttpResponseRedirect("/orders/")
    return HttpResponse(u'{"result":-99, "desc":"无效请求"}', content_type="application/json")


def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})
