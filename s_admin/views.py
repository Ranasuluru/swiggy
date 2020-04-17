from django.shortcuts import render,redirect

from django.contrib import messages
from s_admin.forms import *
from s_admin.models import *

def admin_login(request):
    return render(request,"s_admin/login.html")


def admin_login_check(request):
    ausername = request.POST.get("admin_username")
    apassword = request.POST.get("admin_password")
    try:
        AdminLoginModel.objects.get(username=ausername,password=apassword)
        request.session['status'] = True
        return redirect('admin_home')

    except AdminLoginModel.DoesNotExist:
        messages.error(request,"Sorry Invalid Details")
        return redirect('admin_login')


def admin_home(request):
    return render(request, "s_admin/admin_home.html")


def admin_logout(request):
    request.session['status'] = False
    return redirect('admin_login')


def open_state(request):
    return render(request,'s_admin/open_state.html',{"sf":StateForm(),"sdata":StateModel.objects.all()})


def save_state(request):
    sf = StateForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_state')
    else:
        return render(request,"s_admin/open_state.html",{"sf":sf})


def update_state(request):
    sno = request.GET.get("sno")
    sname = request.GET.get("sname")
    d1 = {"sno":sno,"sname":sname}
    return render(request,"s_admin/open_state.html",{"update_data":d1,"sdata":StateModel.objects.all()})


def update_state_data(request):
    sno = request.POST.get("s1")
    sname = request.POST.get("s2")
    StateModel.objects.filter(state_no = sno).update(state_name=sname)
    return redirect('open_state')


def delete_state(request):
    sno = request.GET.get("sno")
    StateModel.objects.filter(state_no=sno).delete()
    return redirect('open_state')


def open_city(request):
    return render(request,'s_admin/open_city.html',{"sf":CityForm(),"sdata":CityModel.objects.all()})


def save_city(request):
    sf = CityForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_city')
    else:
        return render(request, "s_admin/open_city.html", {"sf": sf})


def update_city(request):
    cno = request.GET.get("cno")
    cname = request.GET.get("cname")
    d1 = {"sno": cno,"sname": cname}
    return render(request,"s_admin/open_city.html",{"update_data": d1,"cdata": CityModel.objects.all()})


def update_city_data(request):
    cno = request.POST.get("s1")
    cname = request.POST.get("s2")
    CityModel.objects.filter(state_no=cno).update(state_name=cname)
    return redirect('open_city')


def delete_city(request):
    sno = request.GET.get("sno")
    CityModel.objects.filter(state_no=sno).delete()
    return redirect('open_city')


def open_area(request):
    return render(request, 's_admin/open_area.html', {"sf": AreaForm(), "sdata": AreaModel.objects.all()})


def save_area(request):
    sf = AreaForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_area')
    else:
        return render(request, "s_admin/open_area.html", {"sf": sf})

def update_area(request):
    cno = request.GET.get("cno")
    cname = request.GET.get("cname")
    d1 = {"sno": cno,"sname": cname}
    return render(request,"s_admin/open_area.html",{"update_data": d1,"cdata": AreaModel.objects.all()})


def update_area_data(request):
    area_no = request.POST.get("s1")
    area_name = request.POST.get("s2")
    AreaModel.objects.filter(area_no=area_no).update(area_name=area_name)
    return redirect('open_area')


def delete_area(request):
    area_no = request.GET.get("sno")
    AreaModel.objects.filter(area_no=area_no).delete()
    return redirect('open_area')


def open_type(request):
    return render(request, 's_admin/open_type.html', {"sf": RestaurantTypeForm(), "sdata": RestaurantTypeModel.objects.all()})


def save_type(request):
    sf = RestaurantTypeForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_type')
    else:
        return render(request, "s_admin/open_type.html", {"sf": sf})


def update_type(request):
    type_no = request.GET.get("cno")
    type_name = request.GET.get("cname")
    d1 = {"sno": type_no,"sname": type_name}
    return render(request,"s_admin/open_type.html",{"update_data": d1,"sdata": RestaurantTypeModel.objects.all()})


def update_type_data(request):
    type_no = request.POST.get("s1")
    type_name= request.POST.get("s2")
    RestaurantTypeModel.objects.filter(no=type_no).update(type_name=type_name)
    return redirect('open_type')


def delete_type(request):
    type_no = request.GET.get("sno")
    RestaurantTypeModel.objects.filter(no=type_no).delete()
    return redirect('open_type')
