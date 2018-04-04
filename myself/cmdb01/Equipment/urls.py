#coding:utf-8
from django.conf.urls import url
import views
urlpatterns = [
        url(r'^vueTest', views.vueTest),
        url(r'^eqList/$', views.eqList),
        url(r'^eqDatas/(\d+)', views.eqDatas),
        url(r'^equip_api', views.equip_api),
        url(r'^gateone', views.gateone),
        url(r'^addEquipment', views.addEquipment),
        url(r'^Terminal/(\d{1,3})', views.Terminal),
        url(r'^get_auth_obj', views.get_auth_obj),
        url(r'^morris', views.morris),

    ]