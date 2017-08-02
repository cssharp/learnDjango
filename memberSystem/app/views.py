from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Member
from django.http import HttpResponse
from django.core import serializers
import json

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
