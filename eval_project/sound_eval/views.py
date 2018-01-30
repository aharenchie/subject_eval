from django.shortcuts import render
from django.views.generic import TemplateView
from sound_eval.management.commands.lib.PyAudio import *
import os,time,csv

WORKSPACE_DIR=os.path.dirname(os.path.abspath(__file__))

def index(request):
    # Question_id の初期化
    return render(request, 'sound_eval/top.html')

def practice_announcement(request):
    return render(request, 'sound_eval/practice_announcement.html')

def practice(request):

    # 定義
    question_id = 1 # 質問ナンバー
    data_dir= WORKSPACE_DIR + '/management/data/eval' + str(question_id) + '/' # 音声データ
    output_file = WORKSPACE_DIR + '/static/files/test.csv' # 出力ファイル
    
    if request.method == 'POST':
        if 'play_button' in request.POST:            
            time_data=time.time() # 時間計測
            
            main_func(data_dir) # 音声再生           
            
            with open(output_file,'a',newline='') as f: # 結果の書き込み
               writer = csv.writer(f, lineterminator='\n')
               writer.writerow([question_id,data_dir,'',time_data,'play_button'])
            
        elif 'send_button' in request.POST:
            time_data=time.time() # 時間計測

            select_id = request.POST['select_id'] # 選択データの取得(A or B)  
            
            with open(output_file,'a',newline='') as f: # 結果の書き込み 
               writer = csv.writer(f, lineterminator='\n')
               writer.writerow([question_id,data_dir,select_id,time_data,'send_button'])
            
            # Question_idのインクリメント
            return render(request,'sound_eval/end.html') # 次の実験ページへ,idを渡す？

    return render(request, 'sound_eval/practice.html')


def end(request):
    return render(request, 'sound_eval/end.html')

