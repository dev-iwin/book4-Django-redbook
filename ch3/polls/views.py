from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Question, Choice
from django.views import generic
import logging
# logger = logging.getLogger(__name__)

#--- Class-based GenericView
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """최근 생성된 질문 5개를 반환함"""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

#--- Function-based View

def vote(request, question_id):
    logger.debug("vote().question_id: %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 설문 투표 폼을 다시 보여줌
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 정상으로 처리하였으면
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션을 처리함
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


'''
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id): # 두번째 인자가 필요했음
    question = get_object_or_404(Question, pk=question_id)  # 여기가 초이스 맞아? 아니었음
    return render(request, 'polls/detail.html', {'question': question})  # 왜 context에 대입 안 했지?(단순 질문)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # 퀘스천 객체 맞아? 맞음
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
        
        # POST 데이터를 정상으로 처리하였으면
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션을 처리함
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  # : 맞음

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
        
'''