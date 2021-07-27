from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import Comment
from .models import Temperatures


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
    if check_password(password, user.password):
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
        encry_password = make_password(password)
        newUser = User(username=username, password=encry_password,
                       time_created=now, last_login=now)
        newUser.save()
        return HttpResponse(json.dumps(dic))
    if user is not None:
        dic['status'] = "Failed"
        dic['message'] = "User exist"
        return HttpResponse(json.dumps(dic))


@csrf_exempt
def forecast(request):  #指定城市未来七天温度预测
    content = json.loads(request.body)
    city = content['city']
    print(city)
    x = []
    ymin = []
    yavg = []
    ymax = []
    now = datetime.datetime.now()
    for i in range(1, 8, 1):
        d = (now + timedelta(days=i))
        day_text = ("%s/%s/%s" % (d.year, d.month, d.day))
        print(day_text)
        info = Temperatures.objects.get(city=city, date=day_text)
        x.append(info.date)
        ymin.append(info.tmin)
        yavg.append(info.tavg)
        ymax.append(info.tmax)

    dic = {'status': "Success", 'x': x, 'ymin': ymin, 'yavg': yavg, 'ymax': ymax}

    return HttpResponse(json.dumps(dic))


@csrf_exempt
def everyday(request):  #指定日期指定城市查询天气
    content = json.loads(request.body)
    date = content['date']
    city = content['city']
    print(date)
    print(city)
    d = datetime.datetime.strptime(date, "%Y/%m/%d")
    day_text = ("%s/%s/%s" % (d.year, d.month, d.day))
    print(day_text)

    try:
        info = Temperatures.objects.get(city=city, date=day_text)
        tavg = info.tavg
        tmin = info.tmin
        tmax = info.tmax
        weather = info.con
    except Temperatures.DoesNotExist:
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
           'tmax': tmax, 'weather': weather, 'wearing': wearing,
           'travel': travel, 'city': city, 'date': date}

    return HttpResponse(json.dumps(dic))


@csrf_exempt
def send_comment(request):
    dic = {}
    if request.method != 'POST':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))

    try:
        post_content = json.loads(request.body)
        print(post_content['user_id'])

        user_id = int(post_content['user_id'])
        text = post_content['text']
        if text == "":
            dic['status'] = "Failed"
            dic['message'] = "No Input"
            return HttpResponse(json.dumps(dic))
        if len(text) > 60:
            dic['status'] = "Failed"
            dic['message'] = "Too long"
            return HttpResponse(json.dumps(dic))
        user = User.objects.get(id=user_id)
    except (KeyError, json.decoder.JSONDecodeError):
        dic['status'] = "Failed"
        dic['message'] = "No Input"
        return HttpResponse(json.dumps(dic))
    except User.DoesNotExist:
        dic['status'] = "Failed"
        dic['message'] = "Wrong User_id"
        return HttpResponse(json.dumps(dic))

    dic['status'] = "Success"
    newComment = Comment(user_id=user, text=text)
    newComment.save()
    return HttpResponse(json.dumps(dic))


@csrf_exempt
def load_comments(request):
    comments = Comment.objects.all()

    if comments.count() == 0:
        dic = {'status': "Failed", 'message': "no comments"}
        return HttpResponse(json.dumps(dic))

    array = []
    if comments.count() > 60:
        sixtyComs = comments.order_by('createTime')[:60]
        for com in sixtyComs:
            array.append(com.text)
    else:
        for com in comments:
            array.append(com.text)
    array.reverse()
    dic = {'status': "success", 'comments_array': array}

    return HttpResponse(json.dumps(dic))




