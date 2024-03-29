from django.shortcuts import render,redirect
from mysite.models import Post,Postdetail,User
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from mysite.form import UserRegisterForm,LoginForm
from mysite import form,models
from .models import Book
from .filters import BookFilter


# Create your views here.
def homepage(request):
    #posts = Post.objects.all()
    postdetails = Postdetail.objects.all()
    now = datetime.now()
    return render(request,'index.html',locals())

def showpost(request,slug):
    post=Postdetail.objects.get(slug=slug)
    if post !=None:
        return render(request,'post.html',locals())
    else:
        return redirect("/")

def newinformation(request):
    return render(request, 'newinformation.html')

from django.contrib.auth.models import User

def index(request):
    if 'username' in request.session and request.session['username'] != None:
        user_id = request.session['username']
    return render(request, 'index.html', locals()) 

from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        login_form = UserRegisterForm(request.POST)
        if login_form.is_valid():
            user_id = request.POST['user_id'].strip()
            user_pass = request.POST['user_pass']
            user_password_confirm = request.POST['user_password_confirm']
            if user_pass == user_password_confirm:
                if not User.objects.filter(username=user_id).exists():
                    user = User.objects.create_user(user_id, '', user_pass)
                    user.save()
                    message = "註冊成功! 請點選「返回登入」進行登入"
                    #return redirect('/login/')
                else:
                    message = "帳號已經存在"
            else:
                message = "密碼不一致"
        elif not login_form.is_valid():
            print(login_form.errors)
            message = "請檢查輸入的欄位內容"
    else:
        register_form = form.LoginForm()

    return render(request, 'register.html', locals())
    
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', locals())
        
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = request.POST['user_id'].strip()
            user_pass = request.POST['user_pass']
            print(f'user_id:{user_id}, pass: {user_pass}')
            user = authenticate(username=user_id, password=user_pass)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    message = '成功登入了'
                    return redirect('/user/')
                else:
                    message = '帳號尚未啟用'
            else:
                message = '登入失敗'
        return render(request, 'login.html', locals())
    else:
        message = 'error'
        return render(request, 'login.html', locals())

def userhome(request):
    #posts = Post.objects.all()
    postdetails = Postdetail.objects.all()
    now = datetime.now()
    return render(request,'userindex.html',locals())

def userdata(request):
    #posts = Post.objects.all()
    postdetails = Postdetail.objects.all()
    now = datetime.now()
    return render(request,'userdata.html',locals())

def bookroom(request):
    #posts = Post.objects.all()
    postdetails = Postdetail.objects.all()
    now = datetime.now()
    return render(request,'bookroom.html',locals())

@login_required
def profile(request):
    user = request.user
    return render(request, 'userheader.html', {'user': user})

def usershowpost(request,slug):
    post=Postdetail.objects.get(slug=slug)
    if post !=None:
        return render(request,'userpost.html',locals())
    else:
        return redirect("/")

def book(request):
    books = Postdetail.objects.all()
 
    bookFilter = BookFilter(queryset=books)
 
    if request.method == "POST":
        bookFilter = BookFilter(request.POST, queryset=books)
 
    context = {
        'bookFilter': bookFilter
    }
 
    return render(request, 'search.html', context)

def usersearch(request):
    #posts = Post.objects.all()
    postdetails = Postdetail.objects.all()
    now = datetime.now()
    
    return render(request,'usersearch.html',locals())

def loginAdmin(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'loginAdmin.html', locals())
        
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = request.POST['user_id'].strip()
            user_pass = request.POST['user_pass']
            print(f'user_id:{user_id}, pass: {user_pass}')
            user = authenticate(username=user_id, password=user_pass)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    message = '成功登入了'
                    return redirect('/adminhome/')
                else:
                    message = '帳號尚未啟用'
            else:
                message = '登入失敗'
        return render(request, 'loginAdmin.html', locals())
    else:
        message = 'error'
        return render(request, 'loginAdmin.html', locals())
    
def adminhome(request):
    #posts = Post.objects.all()
    postdetails = Postdetail.objects.all()
    now = datetime.now()
    return render(request,'adminindex.html',locals())

def adminshowpost(request,slug):
    post=Postdetail.objects.get(slug=slug)
    if post !=None:
        return render(request,'adminpost.html',locals())
    else:
        return redirect("/")
    
def addbook(request):
    posts = Postdetail.objects.filter(enable=True).order_by('-Publiccationdate')[:30]

    if request.method == 'GET':
        return render(request, 'addbook.html', locals())
    elif request.method == 'POST':
        bookname = request.POST['bookname']
        author = request.POST['author']
        state = request.POST['state']
        post = Postdetail(Bookname=bookname, Author=author, State=state)
        post.save()
        message = f'成功儲存[{bookname}]!'
        return render(request, 'addbook.html', locals())
    else:
        message = 'post/get 出現錯誤'
        return render(request, 'addbook.html', locals())