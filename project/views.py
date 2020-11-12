from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # -----中间放调用接口获得参数-------


    # -----中间放调用接口获得参数-------

    #直接返回一段文字
    # return HttpResponse('hello word')
    #返回html地址链接，html存在project包的templates文件夹，系统会自动识别
    return render(request,'test.html')