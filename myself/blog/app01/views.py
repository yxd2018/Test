from django.shortcuts import render
from app01.models import *

# Create your views here.

def index(request):
    #home
    h_list = Home1.objects.all()
    h_list1 = h_list[0]
    h_list2 = h_list[1]
    h_list3 = h_list[2]
    h_list4 = h_list[3]
    h_list5 = h_list[4]
    h_list6 = h_list[5]

    #aboutus1
    obj_list1 = Aboutus1.objects.all()
    #aboutus2
    obj_list2 = Aboutus2.objects.all()

    #scenic1
    s_list1 = Scenic1.objects.all()
    slist1 = s_list1[0]
    #scenic2
    s_list2 = Scenic2.objects.all()
    slist2 = s_list2[0]
    #scenic3
    s_list3 = Scenic3.objects.all()
    slist3 = s_list3[0]

    #industries
    in_list = Industries.objects.all()


    # print slist1,slist2,slist3
    # print s_list1
    return render(request, 'index.html', locals())

def index2(request, nid):
    nid = int(nid)
    content = Industries.objects.get(id=nid)

    # print content.title
    return render(request, 'index2.html', locals())