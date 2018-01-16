
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
=======
>>>>>>> 8fef4b0bb4bd2930c78ef7f0ddcc5b1b878ee835

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTopicForm
from .models import Board, Topic, Post
<<<<<<< HEAD
from django.http import HttpResponse, Http404    


=======
from django.http import HttpResponse, Http404                        
>>>>>>> 8fef4b0bb4bd2930c78ef7f0ddcc5b1b878ee835
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

<<<<<<< HEAD
@login_required
=======
>>>>>>> 8fef4b0bb4bd2930c78ef7f0ddcc5b1b878ee835
def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})



