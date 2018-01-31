# subject_eval

## 環境
Django 2.0
Python 3.5 ~

## 実行方法
git clone subject_eval
cd eval_project
python manage.py runserver

下記のURLにアクセスする
http://127.0.0.1:8000/eval/

## 実行準備
1. 質問音声データをフォルダに格納する。
(subject_eval/eval_project/sound_eval/static/media)
2. DBへのデータ挿入する

## データ場所
質問音声データのPATH
→ subject_eval/eval_project/sound_eval/static/media

結果出力のPATH
→ subject_eval/eval_project/sound_eval/static/files 

## DBへのデータ挿入

```質問情報
# python manage.py shell
In [1]: from sound_eval.models import Question
In [2]: q = Question.objects.get(id=1)
In [3]: print(q.question_id,q.question_max)
3 100
In [4]: q.question_id = 1
In [5]: q.question_max = 3 # 質問の最大数を保存
In [6]: print(q.question_id,q.question_max)
1 3
In [7]: q.save()
```
```時間情報
# python manage.py shell 
In [1]: from sound_eval.models import Time_data
In [3]: import time
In [4]: t = Time_data()
In [5]: t.start_time = time.time()
In [7]: t.save()
In [8]: t = Time_data.objects.get(id=1)
In [10]: print(t.start_time)
```