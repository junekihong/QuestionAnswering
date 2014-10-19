from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
#from django.template import RequestContext, loader

from questions.models import Choice, TextQuestion, AudioQuestion

class IndexView(generic.ListView):
    template_name = 'questions/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the questions. Ordered by number of votes.
        """
        return TextQuestion.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-votes')


class DetailView(generic.DetailView):
    model = TextQuestion
    template_name = 'questions/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return TextQuestion.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = TextQuestion
    template_name = 'questions/results.html'


def vote(request, question_id):
    p = get_object_or_404(TextQuestion, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'questions/detail.html', {
            'textquestion': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        p.votes += 1
        p.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('questions:results', args=(p.id,)))


