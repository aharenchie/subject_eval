from django.urls import path
from . import views 

app_name = 'sound_eval'
urlpatterns = [
    path('', views.index),
    path('practice_announcement/', views.practice_announcement,name='practice_announcement'),
    path('practice/',views.practice,name='practice'),
]    
