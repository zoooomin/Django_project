from django.db import models
from django.contrib.auth.models import  User
class Question(models.Model):
    #author-foreignkey: user가 삭제될경우 이 작성자의 게시물 모두 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    '''질문'''
    #질문의 제목
    subject = models.CharField(max_length=200)
    #질문의 내용
    content = models.TextField()
    #질문을 작성한 일시
    create_date = models.DateTimeField()
    #질문을 수정한 일시
    modify_date = models.DateTimeField(null=True, blank=True)
    #추천인 속성
    voter = models.ManyToManyField(User, related_name='voter_question')
    def __str__(self):
        return self.subject

class Answer(models.Model):
    # author-foreignkey: user가 삭제될경우 이 작성자의 게시물 모두 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    '''답변'''
    #어떤 질문에 대한 답변?
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #답변의 내용
    content = models.TextField()
    #답변을 작성할 일시
    create_date = models.DateTimeField()
    #답변을 수정한 일시
    modify_date = models.DateTimeField(null=True, blank=True)
    #추천인 속성
    voter = models.ManyToManyField(User, related_name='voter_answer')