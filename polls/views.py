from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Question
from django.db.models import Sum

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Cavab seçməmisiniz.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id=question.id)
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    total_votes = question.choice_set.aggregate(total=Sum('votes'))['total'] or 0
    context = {
        'question': question,
        'total_votes': total_votes,
    }
    return render(request, 'polls/results.html', context)