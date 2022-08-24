from turtle import title
from django.shortcuts import render, HttpResponse
from django.contrib.auth import logout
from . forms import CreatorsForm, LoginForm, SubjectForm, ChapterForm, SubChapterForm
from .models import Creators,Subject, Chapter, SubChapter
from django.contrib import messages
def index(request):
    if request.method  =="POST":
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        creator = Creators(fullname= name, email =email, password =password, address =address)
        creator.save()
        messages.success(request,'Account Created Successfully!')
        return render(request,'app/index.html')

    else:
        fms= CreatorsForm()
        return render(request,'app/index.html',{'fm':fms})

def login(request):
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        creater = Creators.objects.get(email = email, password =password)
        print(creater.type)
        if(creater.type == 'admin'):
            return render(request,'app/details.html')
        else:
            return HttpResponse("you are not admin ")
    else:
        fms = LoginForm()
        return render(request,'app/login.html',{'fm':fms})

def addsubject(request):
    if request.method == "POST":
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        price  = request.POST.get('price')
        subject = Subject(title= title, writer = writer, price= price)
        subject.save()
        return render(request,'app/details.html')
    else:
        subform = SubjectForm()
        return render(request,'app/subjectform.html',{'subform':subform})

def choosesubject(request):
    subject = Subject.objects.all()
    return render(request,'app/chosesubject.html',{'data':subject})

def addchapter(request):
    if request.method == "POST":
        subject_id = request.POST['subjectname']
        print(subject_id)
        chapter = Subject.objects.get(id =subject_id )
        print(chapter)
        name = request.POST.get('chaptername')
        page = request.POST.get('pagenumber')
        writer = request.POST.get('writername')
        chapter = Chapter(subject =chapter, chaptername= name, pagenumber= page, writername= writer )
        chapter.save()
        return render(request,'app/details.html')
    else:
        subject = Subject.objects.all()
        fm = ChapterForm()
        return render(request,'app/chapter.html',{'data':subject, 'fm':fm})

def subchapter(request):
    if request.method =="POSt":
        chaptername = request.POST.get('chapter')
        subchaptername = request.POST.get('subchaptername')
        writer = request.POST.get('writername')
        page = request.POST.get('pagenumber')
        subchapters = SubChapter(chapter= chaptername, subchaptername =subchaptername, writername= writer, pagenumber= page)
        subchapters.save()
        return render(request,'app/details.html')
        
    else:
        chapter = Chapter.objects.all()
        print(chapter)
        fm= SubChapterForm()
        return render(request,'app/subchapterform.html', {'chapter':chapter, 'fm':fm})
        
def logout_view(request):
    logout(request)