import hashlib
import random
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from flask import json
import time

all_good = open('solved.txt', 'a+', 1)

mstime = lambda: int(round(time.time() * 1000))

@csrf_exempt
def check_username_password(request, *args, **kwargs):
    start_time = mstime()
    if request.GET != {}:
        data = request.GET
    else:
        data =request.POST
    username = data.get('username', None)
    password = data.get('password', None)
    expected_password = 'packet'
    if username is None or password is None:
        response = {'status': 'failure'}
    else:
        while len(password) > 0 and len(expected_password) > 0:
            front_correct = expected_password[0]
            expected_password = expected_password[1:]
            front_given = password[0]
            password = password[1:]
            if front_correct != front_given:
                response = {'status': 'failure', 'time': mstime() - start_time}
                return HttpResponse(json.dumps(response), content_type="application/json")
            time.sleep(random.random() * .05 + .1)
        if len(password) == 0 and len(expected_password) == 0:
            response = {'status': 'success'}
            all_good.write(username)
            all_good.write('\n')
            return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            response = {'status': 'failure', 'time': mstime() - start_time}
            return HttpResponse(json.dumps(response), content_type="application/json")

