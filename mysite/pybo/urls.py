from django.urls import path

from . import views

#서로 다른 앱에서 동일한 URL별칭 사용으로 중복이 발생하는 문제를 막기 위해
app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/',views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create')
]