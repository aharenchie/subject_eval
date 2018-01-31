from django.shortcuts import render
from django.views.generic import TemplateView
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
    data_dir= WORKSPACE_DIR + '/management/data/practice/' # 音声データ

    if request.method == 'POST':
        # == 送信ボタン押下 ==
        if 'send_button' in request.POST:
            return render(request,'sound_eval/experiment_announcement.html') 
    
    return render(request, 'sound_eval/practice.html',{'question_id': "practice"})

def experiment_announcement(request):
    return render(request,'sound_eval/experiment_announcement.html')

def experiment(request):
    q = Question.objects.get(id=1)
    question_id = q.question_id # 質問ナンバー
    output_file = WORKSPACE_DIR + '/static/files/result.csv' # 出力ファイル
    data_dir= WORKSPACE_DIR + '/management/data/' + str(question_id) + '/'# 音声データ

    if request.method != 'POST': # 最初のページ
        t = Time_data.objects.get(id=1)
        t.start_time = time.time() # 時間計測                                                                                                           
        t.save()
        
    if request.method == 'POST': # 2回目以降
        # == 送信ボタン押下 ==
        if 'send_button' in request.POST:
            t = Time_data.objects.get(id=1)
            q = Question.objects.get(id=1)
            
            time_data= time.time() - t.start_time # 時間計測
            select_type = request.POST['select_type'] # 選択データの取得(A or B)

            with open(output_file,'a',newline='') as f: # 結果の書き込み
                writer = csv.writer(f, lineterminator='\n')
                writer.writerow([question_id,data_dir,select_type,time_data])

            t.start_time = time.time() # 時間計測 
            t.save()
            if question_id < q.question_max:
                question_id += 1
                q.question_id = question_id
                q.save()
                return render(request,'sound_eval/experiment.html',{'question_id': question_id})
            else:
                return render(request, 'sound_eval/end.html')
                        
    return render(request,'sound_eval/experiment.html',{'question_id': question_id})

def end(request):
    return render(request, 'sound_eval/end.html')

