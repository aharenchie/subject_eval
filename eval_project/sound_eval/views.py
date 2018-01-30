from django.shortcuts import render
from django.views.generic import TemplateView
from sound_eval.management.commands.lib.PyAudio import *
from .models import Question,Time_data
import os,time,csv

WORKSPACE_DIR=os.path.dirname(os.path.abspath(__file__))
    
def index(request):
    # Question_id の初期化
    q = Question.objects.get(id=1)
    q.question_id = 1
    q.save()
    return render(request, 'sound_eval/top.html')

def practice_announcement(request):
    return render(request, 'sound_eval/practice_announcement.html')

def practice(request):
    q = Question.objects.get(id=1)
    question_id = q.question_id # 質問ナンバー
    data_dir= WORKSPACE_DIR + '/management/data/eval' + str(question_id) + '/' # 音声データ
    output_file = WORKSPACE_DIR + '/static/files/test.csv' # 出力ファイル
    
    if request.method == 'POST':
        # == 再生ボタン押下 ==
        if 'play_button' in request.POST:
            t = Time_data.objects.get(id=1)

            time_flag = t.flag # フラグ
            
            if time_flag is not True:
                t.start_time = time.time() # 時間計測
                t.flag = True
                
            main_func(data_dir) # 音声再生  
                
            t.save()

        # == 送信ボタン押下 ==
        elif 'send_button' in request.POST:
            t = Time_data.objects.get(id=1)
            q = Question.objects.get(id=1)
            
            time_data= time.time() - t.start_time # 時間計測
            select_type = request.POST['select_type'] # 選択データの取得(A or B)
            
            with open(output_file,'a',newline='') as f: # 結果の書き込み 
               writer = csv.writer(f, lineterminator='\n')
               writer.writerow([question_id,data_dir,select_type,time_data])
            
            t.flag = True
            t.save()
            
            #q.question_id = question_id + 1
            q.question_id = question_id
            q.save()
            
            return render(request,'sound_eval/end.html') 
    
    return render(request, 'sound_eval/practice.html')    

def end(request):
    return render(request, 'sound_eval/end.html')

