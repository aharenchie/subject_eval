from django.shortcuts import render
from django.views.generic import TemplateView
from 
def index(request):
    return render(request, 'sound_eval/top.html')

def practice_announcement(request):
    return render(request, 'sound_eval/practice_announcement.html')

def practice(request):
    # ここらへんに選択したときの処理を書く    
    return render(request, 'sound_eval/practice.html')

    
"""
class TopPageView(TemplateView):
    template_name = "sound_eval/top.html"
    
"""
