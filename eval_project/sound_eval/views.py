from django.shortcuts import render
from django.views.generic import TemplateView
from sound_eval.management.commands.lib.PyAudio import *

import asyncio

def index(request):
    return render(request, 'sound_eval/top.html')

def practice_announcement(request):
    return render(request, 'sound_eval/practice_announcement.html')

def practice(request):        
    if request.method == 'POST':
        if 'play_button' in request.POST:
            main_func()
        elif 'send_button' in request.POST:
            return render(request,'sound_eval/end.html')

    return render(request, 'sound_eval/practice.html')

def end(request):
    return render(request, 'sound_eval/end.html')

