from django.shortcuts import render
from django.shortcuts import redirect
from mysite.models import Post,Postdetail,PostdetailTwo
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from mysite.form import UserRegisterForm
from mysite import form,models

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


def login(request):
    if request.method == 'POST':
        login_form = form.LoginForm(request.POST)
        if login_form.is_valid():
            user_id = request.POST['user_id'].strip()
            user_pass = request.POST['user_password']
            try:
                user = User.objects.get(name = user_id)
                if user.password == user_pass:
                    request.session['username'] = user.name
                    request.session['useremail'] = user.email
                    return redirect('/')
                else:
                    message = "密碼錯誤，請再檢查一次"
            except:
                message = "找不到使用者"
        else:
            message = "請檢查輸入的欄位內容"
    else:
        login_form = form.LoginForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.method == 'POST':
        login_form = UserRegisterForm(request.POST)
        if login_form.is_valid():
            user_id = request.POST['user_id'].strip()
            user_pass = request.POST['user_password']
            user_password_confirm = request.POST['user_password_confirm']
            if user_pass == user_password_confirm:
                if not User.objects.filter(username=user_id).exists():
                    user = models.User(user_id = user_id, user_pass = user_pass)
                    user.save()
                    return redirect('/login/')
                else:
                    message = "帳號已經存在"
            else:
                message = "密碼格式不符"
        if not login_form.is_valid():
            print(login_form.errors)
            message = "請檢查輸入的欄位內容"
    else:
        register_form = form.LoginForm()
    return render(request, 'register.html', locals())

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