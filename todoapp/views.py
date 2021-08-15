from django.shortcuts import render,redirect
from .forms import Userdata, Createnewpost
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post


# Create your views here.
def loginpage(request):
    if request.method=='POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request,username=Username,password = Password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'loginpage.html')
    context={}
    return render(request, 'loginpage.html',context)


def signup(request):
    form = Userdata()
    if request.method=='POST':
        form = Userdata(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Try again with different details')
            context={'form':form}
            return render(request,'signup.html',context)
        
    context={'form':form,}
    return render(request,'signup.html',context)


@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    posts = Post.objects.all
    context={'posts':posts}
    return render(request,'home/index.html',context)


@login_required(login_url='login')
def createpost(request):
    user = request.user
    postform = Createnewpost()
    if request.method=='POST':
        if request.user.is_authenticated:
            postform = Createnewpost(request.POST)
            if postform.is_valid():
                post =postform.save(commit=False)
                post.user = request.user
                if request.FILES['post_image']:
                    post.post_image=request.FILES['post_image']
                if request.FILES['post_image1']:
                        post.post_image1=request.FILES['post_image1']
                if request.FILES['post_image2']:   
                        post.post_image2=request.FILES['post_image2']
                post.save()
                print(post)
                context ={"postform":postform,}
                messages.info(request, 'Posted!')
                return redirect('createpost') 
            else:
                print("ERROR : Form is invalid")
                messages.info(request,"ERROR : Form is invalid")
                        

    context ={"postform":postform,}
    return render(request,'createpost.html',context)


@login_required(login_url='login')
def viewposts(request):
    user_posts = Post.objects.filter(user=request.user)
    context ={'posts':user_posts}
    return render(request,'viewposts.html',context)


@login_required(login_url='login')
def loadpost(request,id):
    postdata = Post.objects.get(id=id)
    context ={'postdata':postdata}
    return render(request,'loadpost.html',context)

