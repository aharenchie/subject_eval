from models import Question

questions = Question.objects.all()
for i in questions:
  print(i.question_id)
