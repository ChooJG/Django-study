from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

import random


# Create your views here.
def index(request):
    now = datetime.now()
    # 이후 여기 변수를 index.html로 보냄
    context = {
        'current_date': now
    }
    return render(request, 'first/index.html', context)


def select(request):
    context = {

    }
    return render(request, 'first/select.html', context)


def result(request):
    chosen = int(request.GET['number'])
    results = []
    if 1 <= chosen <= 45:
        results.append(chosen)

    box = []
    for i in range(0, 45):
        if chosen != i + 1:
            box.append(i+1)

    random.shuffle(box)
    while len(results) < 6:
        results.append(box.pop())

    context = {
        "numbers": results
    }

    return render(request, 'first/result.html', context)