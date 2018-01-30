from django.urls import path
from . import views,views2 

app_name = 'sound_eval'
urlpatterns = [
    path('', views.index),
    path('practice_announcement/', views.practice_announcement,name='practice_announcement'),
    path('practice/',views.practice,name='practice'),
    path('practice2/',views2.practice,name='practice2'),
    path('end/',views.end,name='end'),
]    
