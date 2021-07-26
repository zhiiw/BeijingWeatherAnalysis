from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import Rank5
from .models import Prewholeyear
from .models import Beijing
from .models import Try


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
        print(dic)
        return HttpResponse(json.dumps(dic))
    try:
        post_content = json.loads(request.body)
        print(post_content)
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
        print(dic)
        return HttpResponse(json.dumps(dic))
    else:
        dic['message'] = "Wrong Password"
        dic['status'] = "Failed"
        print(dic)
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
def forecast(request):  #北京未来七天温度预测
    content = json.loads(request.body)
    city = content('city')
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
def everyday(request):  #北京未来七天温度预测
    if request.method != 'POST':
        dic = {'status': "Failed", 'message': "Wrong Method"}
        return HttpResponse(json.dumps(dic))

    content = json.loads(request.body)
    date = content['date']
    city = content['city']

    try:
        info = Try.objects.get(city=city, date=date)
        tavg = info.tavg
        tmin = info.tmin
        tmax = info.tmax
        weather = info.con
    except Try.DoesNotExist:
        dic = {'status': "Failed", 'message': "No information"}
        return HttpResponse(json.dumps(dic))

    if tavg > 23:
        wearing = "T-shirts"
    elif tavg > 15:
        wearing = "coats"
    elif tavg > 8:
        wearing = "sweaters"
    else:
        wearing = "down jacket"

    if weather == "rainy":
        travel = "Bring an umbrella"
    elif weather == "cloudy" and 20 < tavg < 28:
        travel = "very suitable"
    elif tavg > 32 or tavg < 5:
        travel = "not very suitable"
    else:
        travel = "suitable"

    dic = {'status': "Success", 'tmin': tmin, 'tavg': tavg,
           'tmax': tmax, 'weather': weather, 'wearing': wearing, 'travel': travel}

    return HttpResponse(json.dumps(dic))


