from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from django.http import HttpResponseNotAllowed
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import  login_required

def index(request):
    page = request.GET.get('page', '1')
    #질문 목록 데이터 얻기
    question_list = Question.objects.order_by('-create_date')
    #페이지당 10개씩 보여주기
    paginator= Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list' : page_obj}
    #render함수는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환함
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    #질문 번호 가져오기
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user #author속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user #author속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)