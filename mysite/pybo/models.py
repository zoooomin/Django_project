from django.db import models
from django.contrib.auth.models import  User
class Question(models.Model):
    #author-foreignkey: user가 삭제될경우 이 작성자의 게시물 모두 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    '''질문'''
    #질문의 제목
    subject = models.CharField(max_length=200)
    #질문의 내용
    content = models.TextField()
    #질문을 작성한 일시
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    # author-foreignkey: user가 삭제될경우 이 작성자의 게시물 모두 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    '''답변'''
    #어떤 질문에 대한 답변?
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #답변의 내용
    content = models.TextField()
    #답변을 작성할 일시
    create_date = models.DateTimeField()