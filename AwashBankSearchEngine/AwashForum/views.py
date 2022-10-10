from django.shortcuts import render  # For rendering static files

# Accepting requests and returning response
from django.http import HttpResponse as response

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# To list all available boards, we have to import Board model from marii app
from .forms import NewTopicForm
from .models import Board, Topic, Post


def forum_home(request):
    #boards = Board.objects.all()
    #return render(request, 'home.html', {'boards': boards})
    
    return response('Awash Bank - The Bank That Nurturing Your Life !\
    #   This is Awash Bank Employeers Discussion Site Thank you for banking with us')

#def board_topics(request):
   # board = get_object_or_404(Board)
   # return render(request, 'topics.html', {'board': board})
   # return render(request, 'topics.html')
   
''' 
def new_topic(request):
    #board = get_object_or_404(Board)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            #topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics')  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'form': form})
    
'''