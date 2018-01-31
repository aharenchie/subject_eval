from django.urls import path
from . import views

app_name = 'sound_eval'
urlpatterns = [
    path('', views.index),
    path('practice_announcement/', views.practice_announcement,name='practice_announcement'),
    path('practice/',views.practice,name='practice'),
    path('playaudio/',views.playaudio,name='playaudio'),
    path('playaudio2/',views.playaudio2,name='playaudio2'),
    path('experiment_announcement/',views.experiment_announcement,name='experiment_announcement'),
    path('experiment/',views.experiment,name='experiment'),
    path('end/',views.end,name='end'),
]    
