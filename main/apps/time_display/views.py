# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime
from datetime import datetime

def index(request):
    time = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p", gmtime()).lstrip('0'),
    }
    return render(request, 'time_display/index.html', time)

# Create your views here.
