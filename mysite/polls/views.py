from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question

# Create your views here.
# def index(request):
#     # Get list of all question objects
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list,}
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    # Grab the question ID
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    # Error handling for not selecting an answer
    except (KeyError, Choice.DoesNotExist):
        # Redisplay question
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You must choose an answer.",
        })
    # Runs if the except block didn't catch (which is a good thing)
    else:
        selected_choice.votes += 1
        # Save results to the database
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))