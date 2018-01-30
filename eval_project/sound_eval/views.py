from django.shortcuts import render
from django.views.generic import TemplateView
from sound_eval.management.commands.lib.PyAudio import *
from .models import Question
import os,time,csv

WORKSPACE_DIR=os.path.dirname(os.path.abspath(__file__))

def index(request):
    # Question_id の初期化,
    question = Question()
    question.question_id = 1
    
    return render(request, 'sound_eval/top.html')

def practice_announcement(request):
    return render(request, 'sound_eval/practice_announcement.html')

def practice(request):
    # 定義
    q = Question.objects.get(id=1)
    question_id = q.question_id # 質問ナンバー
    
    data_dir= WORKSPACE_DIR + '/management/data/eval' + str(question_id) + '/' # 音声データ
    output_file = WORKSPACE_DIR + '/static/files/test.csv' # 出力ファイル
    
    if request.method == 'POST':
        if 'play_button' in request.POST:            
            time_data=time.time() # 時間計測
            main_func(data_dir) # 音声再生           
            
        elif 'send_button' in request.POST:
            time_data=time.time() # 時間計測

            select_type = request.POST['select_type'] # 選択データの取得(A or B)  
            
            with open(output_file,'a',newline='') as f: # 結果の書き込み 
               writer = csv.writer(f, lineterminator='\n')
               writer.writerow([question_id,data_dir,select_type,time_data])
            
            # Question_idのインクリメント
            #q.question_id = question_id + 1
            q.question_id = question_id
            q.save()
            return render(request,'sound_eval/end.html') # 次の実験ページへ,idを渡す？
    
    return render(request, 'sound_eval/practice.html')


def end(request):
    return render(request, 'sound_eval/end.html')

