from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.http import Http404

from feeclBoard.models import *
from account.models import User


# Create your views here.
def index_board(request):
    boards = {'boards': Board.objects.all().order_by('-id')}
    return render(request, 'list.html', boards)

def post(request):
    if request.method == "POST":
        author_id = request.session['user']
        author_info = User.objects.get(id=author_id)
        author_generation = author_info.generation
        author = str(author_generation)+'기'
        title = request.POST.get('title',None)
        content = request.POST.get('content',None)
        res_data={}
        if not(content and title):
            res_data['error'] = '모두 입력해주세요'
        else:
            board = Board(author=author, title=title, content=content,writer_id = author_id)
            board.save()
            return HttpResponseRedirect(reverse('index_board'))
        return render(request,'post.html',res_data)
    else:
        return render(request,'post.html')

def detail_board(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    post=get_object_or_404(Board, pk=id)
    user_id = request.session['user']
    comments = Comment_Board.objects.filter(post=post)
    default_view_count=board.view_count
    board.view_count=default_view_count+1
    board.save()
    return render(request, 'detail.html', {'board': board, 'comments':comments,'user_id':user_id})


""" class BoardUpadteView(UpdateView):
    model=Board
    fields=['title', 'author', 'content']
    template_name_suffix="_update"
 """

def delete_board(request,pk):
    Board.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse('index_board'))

def to_update_board(request,pk):
    board = Board.objects.get(id=pk)
    return render(request, 'feeclBoard/board_update.html', {'board':board})

def update_board(request,pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.save()
        comments = Comment_Board.objects.filter(post=board)
        user_id = request.session['user']
        return render(request, 'detail.html', {'board': board, 'comments':comments,'user_id':user_id})
    else:
        return render(request, 'feeclBoard/board_update.html')


def comment_write(request, pk):
    if request.method=='POST':
        post=get_object_or_404(Board, pk=pk)
        content=request.POST.get('content')
        user_id = request.session['user']
        writer_info = User.objects.get(id=user_id)
        writer_generation = writer_info.generation
        if len(content)>0:
            new_Comment = Comment_Board(post=post, comment_contents=content,comment_writer = writer_generation,comment_writer_id = user_id)
            new_Comment.save()
        board = Board.objects.get(id=pk)
        comments = Comment_Board.objects.filter(post=post)
        return render(request, 'detail.html',{'pk':pk,'comments':comments,'board':board,'user_id':user_id})
    else:
        return HttpResponse('error')

def logout(request):
    request.session.pop('user')
    return redirect('/')

""" def home(request):
    user_pk = request.session.get('user') #login함수에서 추가해준 requests.session['user'] = fuser.id

    if user_pk: #세션에 user_pk 정보가 존재하면
        fuser = User.objects.get(pk=user_pk)
        return render(request,'feeclstar/index.html')
        #return HttpResponse(fuser.generation) #해당 유저의 Fuser모델의 username 전달

    return HttpResponse("로그인 성공") #세션에 유저 정보 없으면 그냥 home으로
 """

def delete_comment(request,pk,pk2):
    Comment_Board.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse('detail_board',kwargs={'id':pk2}))