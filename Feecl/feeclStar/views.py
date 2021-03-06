from django.shortcuts import render,redirect 
from .models import Subject,Comment
from account.models import User
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect


def subjectList(request):
    try:
        select_semester = request.GET['semester']
        if select_semester == 'none':
                subject = Subject.objects.all().order_by('-subject_star')
        elif select_semester == 'one':
            subject = Subject.objects.filter(subject_semester = 1).order_by('-subject_star')
        elif select_semester == 'two':
            subject = Subject.objects.filter(subject_semester = 2).order_by('-subject_star')
        writer_id = request.session['user']
        return render(request,'feeclStar/subject_2_list.html',{'subject':subject,'subjectList':subject,'writer_id':writer_id})
    except:
        try:
            search = request.GET['search']
            subjectList = Subject.objects.filter(subject_name__icontains=search).order_by('-subject_star')
            subject = Subject.objects.all().order_by('-subject_star')
            writer_id = request.session['user']
            return render(request,'feeclStar/subject_2_list.html',{'subject':subject,'subjectList':subjectList,'writer_id':writer_id}) 
        except:
            subject = Subject.objects.all().order_by('-subject_star')
            writer_id = request.session['user']
            return render(request,'feeclStar/subject_2_list.html',{'subject':subject,'subjectList':subject,'writer_id':writer_id})
        
def detail(request,pk):
    writer_id = request.session['user']
    subject = Subject.objects.get(pk=pk)
    comment = Comment.objects.filter(subject_id=subject)
    total = 0
    for i in comment:
        total += i.comment_star
    if total != 0:
        subject_star = total/len(comment)
        subject.subject_star = round(subject_star,2)
        subject.save()
    elif total == 0:
        subject.subject_star = 0
        subject.save()
    return render(request,'feeclStar/subject_2_detail.html',{'subject':subject,'comment':comment,'pk':writer_id})

def delete(request,pk,pk2):
    Comment.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse('detail',kwargs={'pk':pk2}))

def create(request,pk):
    if request.method == "POST":
        comment_text = request.POST.get('comment_text',None)
        comment_star = request.POST.get('comment_star',None)
        if comment_star != None:
            comment_starWidth = int(comment_star)*20
        
        writer_id = request.session['user']
        writerInfo = User.objects.get(id = writer_id)
        writer_generation = writerInfo.generation
        subject_id = Subject.objects.get(id = pk)
        res_data={}
        try:
            CommentExist = Comment.objects.get(writer_id = writer_id)
            if CommentExist.subject_id.id == pk:
                res_data['error'] = '?????? ????????? ?????? ???????????????'
                return render(request,'feeclStar/subject_2_comment.html',res_data)
        except:
            pass
        if not(comment_star and comment_text):
            res_data['error'] = '?????? ??????????????????'
        else:
            write = Comment(comment_text=comment_text, comment_star=comment_star,subject_id = subject_id,comment_starWidth = comment_starWidth,writer_id = writer_id,writer_generation = writer_generation)
            write.save()
            return HttpResponseRedirect(reverse('detail',kwargs={'pk':pk}))

        return render(request,'feeclStar/subject_2_comment.html',res_data)
    else:
        return render(request,'feeclStar/subject_2_comment.html')

def logout(request):
    request.session.pop('user')
    return redirect('/')
