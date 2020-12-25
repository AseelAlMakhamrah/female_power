from django.shortcuts import render,redirect
from django.contrib import messages
from . import models
from .models import Profile, User

def index(request):
    if 'user_id' in request.session:
        return redirect( '/allpostcommunity')
    return render(request,'welcom.html')


def allpostcommunity(request):
    if 'user_id' in request.session:
        return render(request,'allpostcommunity.html')
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

def show(request):
    return render(request, "community.html")

def profile_edit(request):
    return render(request,"profile.html")

def profile_view(request):
    return render(request,"profile_view_mode.html")

def save_profile_changes(request):
    name = request.POST['name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    country = request.POST['country']
    education = request.POST['education']
    edu_from = request.POST['edu-from']
    edu_to = request.POST['edu-to']
    experience = request.POST['experience']
    exp_from = request.POST['exp-from']
    exp_to = request.POST['exp-to']
    skills = request.POST['skills']
    links = request.POST['links']
    video_url = request.POST['video-demo-url']

    context = {
            "name" : name,
            "email" : email,
            "mobile" : mobile,
            "country" : country,
            "education" : education,
            "edu_from" : edu_from,
            "edu_to" : edu_to,
            "experience" : experience,
            "exp_from" : exp_from,
            "exp_to" : exp_to,
            "skills" : skills,
            "links" : links,
            "video_url" : video_url,
    }
    current_user = User.objects.get(id = request.session['user_id'])
    profile = Profile.objects.create(
    skills = skills,
    education = education,
    education_from = edu_from,
    education_to = edu_to,
    experience = experience,
    experience_from = exp_from,
    experience_to = exp_to,
    links = links,
    video_url = video_url,
    user = current_user)
    profile.save()
    return render(request,"profile_view_mode.html", context)
