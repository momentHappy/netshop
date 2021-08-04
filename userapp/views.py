from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import *
from utils.code import *
from django.core.serializers import serialize
from cart.cartmanager import *


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')
        user = UserInfo.objects.create(uname=uname, pwd=pwd)
        if user:
            request.session['user'] = user
            return HttpResponseRedirect('/user/center')
        return HttpResponseRedirect('/user/register')


class CheckUnameView(View):
    def get(self, request):
        uname = request.GET.get('uname', '')
        userList = UserInfo.objects.filter(uname=uname)
        flag = False
        if userList:
            flag = True
        return JsonResponse({'flag': flag})


class CenterView(View):
    def get(self, request):
        return render(request, 'center.html')


class LogoutView(View):
    def post(self, request):
        # 删除session中登录用户的数据
        if 'user' in request.session:
            del request.session['user']
        return JsonResponse({'delflag': True})


class LoginView(View):
    def get(self, request):
        red = request.GET.get('redirect', '')
        if not red:
            return render(request, 'login.html', {'redirect': red})
        return render(request, 'login.html')

    def post(self, request):
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')
        userList = UserInfo.objects.filter(uname=uname, pwd=pwd)
        if userList:
            request.session['user'] = userList[0]
            red = request.POST.get('redirect')
            if red == 'cart':
                SessionCartManager(request.session).migrateSession2DB()
                return HttpResponseRedirect('/cart/queryAll/')
            elif red == 'order':
                return HttpResponseRedirect('/order/order.html?cartitems=' + request.POST.get('cartitems', ''))

            return HttpResponseRedirect('/user/center/')
        return HttpResponseRedirect('/user/login/')


class LoadCodeView(View):
    def get(self, request):
        img, str = gene_code()
        request.session['sessionCode'] = str
        return HttpResponse(img, content_type='image/png')


class CheckcodeView(View):
    def get(self, request):
        code = request.GET.get('code', '')
        sessionCode = request.session.get('sessionCode', None)
        flag = code == sessionCode
        return JsonResponse({'checkFlag': flag})


class AddressView(View):
    def get(self, request):
        user = request.session.get('user', '')
        addrList = user.address_set.all()
        return render(request, 'address.html', {'addrList': addrList})

    def post(self, request):
        aname = request.POST.get('aname', '')
        aphone = request.POST.get('aphone', '')
        addr = request.POST.get('addr', '')
        user = request.session.get('user', '')

        address = Address.objects.create(aname=aname, aphone=aphone, addr=addr, userinfo=user,
                                         isdefault=(lambda count: True if count == 0 else False)(
                                                 user.address_set.all().count()))
        addrList = user.address_set.all()
        return render(request, 'address.html', {'addrList': addrList})


class LoadAreaView(View):
    def get(self, request):
        pid = request.GET.get('pid', '-1')
        pid = int(pid)
        # 根据父id查询区划信息
        areaList = Area.objects.filter(parentid=pid)
        # 进行序列化
        jareaList = serialize('json', areaList)
        return JsonResponse({'jareaList': jareaList})
