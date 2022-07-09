from django.shortcuts import render

from .models import Topic

# Create your views here.


def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    topics = Topic.objects.get(id=topic_id)
    entries = topics.entry_set.order_by('date_added')
    context = {'topics': topics, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
