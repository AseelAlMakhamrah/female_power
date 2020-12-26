from django.shortcuts import render,redirect
from django.contrib import messages
from . import models


def index(request):
    if 'user_id' in request.session:
        return redirect( '/allpostcommunity')
    return render(request,'welcom.html')


def allpostcommunity(request):
    if 'user_id' in request.session:
        context = {
            'first_name':request.session['first_name'],
            'last_name':request.session['last_name'],
            'posts':models.all_posts(),
            'looged_user':models.logged_user(request.session['user_id'])
        }
        return render(request,'allpostcommunity.html',context)
    return redirect('/')   


def register(request):
    if request.method =='POST':
        errors = models.reg_errors(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = models.register(request.POST)
            if user is not None:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                return redirect('/allpostcommunity')
    return redirect('/')


def login(request):
    if request.method=='POST':
        errors = models.login_errors(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = models.login(request.POST)
            if user:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                    return redirect('/allpostcommunity')
    return redirect('/')


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['first_name']
        del request.session['last_name']
    return redirect('/')

def addpost(request):
    if request.method =='POST':
        errors = models.posts_errors(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            post = models.addpost(request.POST,request.session['user_id'])
            if post is not None:
                return redirect('/allpostcommunity')
    return redirect('/allpostcommunity')





# def profile_edit(request):
#     return render(request,"profile.html")

# def profile_view(request):
#     return render(request,"profile_view_mode.html")


def show(request,id):
    context = {
        'post':models.get_post(id),
        'post_data':models.all_posts(),
    }
    return render(request, "community.html",context)

def community(request):
    context = {
        'user':User.objects.get(id=request.session['user_id']),
    }
    return render (request,'community.html',context)

def addcomment(request,id):
    if request.method == 'POST':
        if 'user_id' in request.session:
            comment = models.addcomment(request.POST,id)
            if comment is not None:
                return redirect('/posts/' + str(id))
    return redirect('/community')




def test(request):
    return render(request, "test.html")