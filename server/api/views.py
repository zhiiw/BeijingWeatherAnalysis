from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import Rank5
from .models import Prewholeyear
from .models import Beijing
from django.core.mail import send_mail

import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from datetime import timedelta


@csrf_exempt
def login(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    try:
        post_content = json.loads(request.body)
        username = post_content['username']
        password = post_content['password']
        user = User.objects.get(username=username)
    except (KeyError, json.decoder.JSONDecodeError):
        dic['status'] = "Failed"
        dic['message'] = "No Input"
        return HttpResponse(json.dumps(dic))
    except User.DoesNotExist:
        dic['status'] = "Failed"
        dic['message'] = "Wrong Username"
        return HttpResponse(json.dumps(dic))
    if password == user.password:

        dic['status'] = "Success"
        dic['user_id'] = user.id
        return HttpResponse(json.dumps(dic))
    else:
        dic['message'] = "Wrong Password"
        dic['status'] = "Failed"
        return HttpResponse(json.dumps(dic))


@csrf_exempt
def register(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    try:
        post_content = json.loads(request.body)
        username = post_content['username']
        password = post_content['password']
        user = User.objects.get(username=username)
    except (KeyError, json.decoder.JSONDecodeError):
        dic['status'] = "Failed"
        dic['message'] = "No Input"
        return HttpResponse(json.dumps(dic))
    except User.DoesNotExist:
        dic['status'] = "Success"
        now = datetime.datetime.now()
        newUser = User(username=username, password=password,
                       time_created=now, last_login=now)
        newUser.save()
        return HttpResponse(json.dumps(dic))
    if user is not None:
        dic['status'] = "Failed"
        dic['message'] = "User exist"
        return HttpResponse(json.dumps(dic))


@csrf_exempt
def trial(request):
    now = datetime.datetime.now().__format__('%Y/%m/%d')
    Rank5.objects.filter(name=now).delete()
    return HttpResponse('OK')


@csrf_exempt
def get_temp(request):
    if request.method != 'POST':
        dic = {'status': "Failed", 'message': "Wrong Method"}
        return HttpResponse(json.dumps(dic))

    x = []
    ymin = []
    yavg = []
    ymax = []
    now = datetime.datetime.now()
    for i in range(1, 8, 1):
        d = (now + timedelta(days=i))
        day_text = ("%s/%s/%s" % (d.day, d.month, d.year))
        info = Prewholeyear.objects.get(date=day_text)
        x.append(info.date)
        ymin.append(info.tmin)
        yavg.append(info.tavg)
        ymax.append(info.tmax)

    dic = {'status': "Success", 'x': x, 'ymin': ymin, 'yavg': yavg, 'ymax': ymax}

    return HttpResponse(json.dumps(dic))


@csrf_exempt
def forecast_Beijing(request):  #北京未来七天温度预测
    if request.method != 'POST':
        dic = {'status': "Failed", 'message': "Wrong Method"}
        return HttpResponse(json.dumps(dic))

    x = []
    ymin = []
    yavg = []
    ymax = []
    now = datetime.datetime.now()
    for i in range(1, 8, 1):
        d = (now + timedelta(days=i))
        day_text = ("%s/%s/%s" % (d.year, d.month, d.day))
        info = Beijing.objects.get(date=day_text)
        x.append(info.date)
        ymin.append(info.tmin)
        yavg.append(info.tavg)
        ymax.append(info.tmax)

    dic = {'status': "Success", 'x': x, 'ymin': ymin, 'yavg': yavg, 'ymax': ymax}

    return HttpResponse(json.dumps(dic))


@csrf_exempt
def Beijing_everyday(request):  #北京未来七天温度预测
    if request.method != 'POST':
        dic = {'status': "Failed", 'message': "Wrong Method"}
        return HttpResponse(json.dumps(dic))

    content = json.loads(request.body)
    date = content['date']
    info = Beijing.objects.get(date=date)
    tmin = info.tmin
    tavg = info.tavg
    tmax = info.tmax
    weather = info.con

    dic = {'status': "Success", 'tmin': tmin, 'tavg': tavg, 'tmax': tmax, 'weather': weather}

    return HttpResponse(json.dumps(dic))


@csrf_exempt
def send(request):
    send_mail('测试', '球球了', '2539496792@qq.com', ['2539496792@qq.com'], fail_silently=False)

    dic = {'status': "Success"}

    return HttpResponse(json.dumps(dic))
