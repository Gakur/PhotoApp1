from django import forms
from django.http import request, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from . forms import ProfileForm, UserForm, ImageForm, CommentForm
from django.contrib.auth.models import User

from myphotos.models import Image, Profile, Comment, Follow

# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    images = Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ImageForm()
    params = {
        'images': images,
        'form': form,
        'users': users,

    }
    return render(request, 'photos/index.html', params)


@login_required(login_url='/accounts/login/')
def comment(request,id):
	
	post = get_object_or_404(Image,id=id)	
	current_user = request.user
	print(post)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = current_user
			comment.pic = post
			comment.save()
			return redirect('index')
	else:
		form = CommentForm()

	return render(request,'photos/comment.html',{"form":form}) 


@login_required(login_url='/accounts/login/')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('upload_profile', username=request.user.username)
    user_posts = user_prof.profile.posts.all()
    
    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False
    params = {
        'user_prof': user_prof,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
    }
    print(followers)
    return render(request, 'photos/user_profile.html', params)


@login_required(login_url='/accounts/login/')
def single_pic(request,pic_id):
	image = Image.objects.get(id= pic_id)

	return render(request, 'single_pic.html',{"image": image})

def like(request):
    image = get_object_or_404(Image, id=request.POST.get('id'))
    is_liked = False
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
        is_liked = False
    else:
        image.likes.add(request.user)
        is_liked = False

    params = {
        'image': image,
        'is_liked': is_liked,
        'total_likes': image.total_likes()
    }
    if request.is_ajax():
        html = render_to_string('like.html', params, request=request)
        return JsonResponse({'form': html})


def search_results(request):
    if 'pic' in request.GET and request.GET["pic"]:
        search_term = request.GET.get("pic")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"pics": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def upload_profile(request):
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        prof_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UserForm(instance=request.user)
        prof_form = ProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'images': images,

    }
    return render(request, 'photos/upload_profile.html', params)


def follow(request, to_follow):
    if request.method == 'GET':
        user_profile3 = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower=request.user.profile, followed=user_profile3)
        follow_s.save()
        return redirect('user_profile', user_profile3.user.username)