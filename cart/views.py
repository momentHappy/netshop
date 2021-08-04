from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from .cartmanager import *


class AddCartView(View):
    def post(self, request):
        request.session.modified = True
        # 获取当前操作类型
        flag = request.POST.get('flag', '')
        if flag == 'add':
            carManagerObj = getCartManger(request)
            carManagerObj.add(**request.POST.dict())
        elif flag == 'plus':
            carManagerObj = getCartManger(request)
            carManagerObj.update(step=1, **request.POST.dict())
        elif flag == 'minus':
            carManagerObj = getCartManger(request)
            carManagerObj.update(step=-1, **request.POST.dict())
        elif flag == 'delete':
            carManagerObj = getCartManger(request)
            carManagerObj.delete(**request.POST.dict())

        return HttpResponseRedirect('/cart/queryAll/')


class CartListView(View):
    def get(self, request):
        carManagerObj = getCartManger(request)
        cartList = carManagerObj.queryAll()
        return render(request, 'cart.html', {'cartList': cartList})
