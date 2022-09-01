from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question #사용할 모델
        fields = ['subject', 'content'] #questionform에서 사용할 question모델의 속성
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels ={
            'content' : '답변내용',
        }
