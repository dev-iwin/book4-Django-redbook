from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Question, Choice

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request):
    question = get_object_or_404(Choice)
    return render(request, 'polls/detail.html', {'question': question})  # 왜 context에 대입 안 했지?

def vote(request, question_id):
    question : get_object_or_404(Question, pk=question_id)  # 퀘스천 객체 맞아?
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여준다.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        '''
        POST 데이터를 정상으로 처리하였으면
        항상 HttpResponseRedirect를 반환하여 리다이렉션을 처리함
        '''
        return HttpResponseRedirect(reverse('polls/results', args=(question.id,))) # : 맞아? / 아니고?

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})