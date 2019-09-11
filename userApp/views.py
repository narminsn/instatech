from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SettingsForm, Profile_image
# Create your views here.
from theShots.forms import UserCreationForm
from theShots.views import common_data
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from . import forms
import uuid
from . import models



User = get_user_model()
context = common_data()


def home_view(request):
    if not request.user.is_authenticated:
        context = common_data()
        context['login_form'] = LoginForm()
        if 'register' in request.POST:
            if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    user.username = user.email
                    user.set_password(request.POST.get('password1'))
                    # user.is_active = False
                    user.save()
                    messages.info(
                        request, 'please verify your email'
                    )
                    return HttpResponse("sdfgh")
                else:
                    context['register_form'] = form
        else:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():

                email = login_form.cleaned_data.get('email')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=email, password=password)
                print("user_af", user)
                if user:
                    if user.is_active:
                        login(request, user)
                        if request.user.check:
                            return HttpResponse('true')
                        else:
                            return redirect('explore-view')

        return render(request, 'index.html', context)
    else:
        return redirect('explore-view')


def settings_view(request):
    context = common_data()
    context['image_form'] = Profile_image()
    context['form'] = SettingsForm(instance=request.user)
    if request.method == 'POST':

        if 'settings' in request.POST:
            form = SettingsForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponse('success')
            else:
                context['form'] = form
        else:
            image_form = Profile_image(request.FILES)
            if image_form.is_valid():
                image_data = request.FILES.get('profile_image')
                request.user.profile_image = image_data
                return HttpResponse('save')

    return render(request, 'setting-profile.html', context)


def profile_view(request):
    context['posts'] = models.PostModel.objects.filter(user=request.user)
    return render(request, 'user-profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('base-view')


def shotadd_view(request):
    if request.user.is_authenticated:
        context['form'] = forms.Shotadd()
        context['image_data'] = str(uuid.uuid4())
        if request.method == 'POST':

            form = forms.Shotadd(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                image_data = request.POST.get('image_data')
                image_list = models.ImageModel.objects.filter(image_token=image_data)
                if image_list:
                    for img in image_list:
                        img.post = post
                        img.save()
                return  redirect('explore-view')
            else:
                context['form'] = form


        return render(request, 'shot-add.html', context)
    else:
        return redirect('base-view')


def shot_add(request):
    if request.method == 'POST':
        img = models.ImageModel.objects.create(
            image=request.FILES.get('file'),
            image_token=request.POST.get('image_data')
        )
        return JsonResponse({
            'pk': img.id,
            'uploaded': True
        })
    else:
        return JsonResponse({
            'uploaded': False
        })


def shotdelete_view(request):
    if request.method == 'POST' and request.is_ajax():
        pk = request.POST.get('remove_object')
        img = models.ImageModel.objects.filter(id=pk).last()
        if img:
            img.delete()
            return JsonResponse({
                'deleted': True
            })
        else:
            return JsonResponse({
                'deleted': False
            })
    else:
        if not request.is_ajax():
            return redirect("base-view")
        return JsonResponse({
            'uploaded': False
        })
    # return render(request, 'shot-add.html', context)


def form_view(request):
    context['form'] = forms.Formm()
    if request.method == 'POST':
        print(request.FILES)
        return HttpResponse('success')
    return render(request,'form.html',context)




def postmodal_view(request, id):
    context = {}

    id = id
    post = models.PostModel.objects.filter(id=id).last()
    context['post'] = post
    context['images'] =  models.PostModel.objects.filter(id=id).last().imagemodel_set.all()
    context['comment_form'] = forms.Comment
    context['comments'] = post.commentmodel_set.all()
    context["form"] = forms.Comment
    if request.method == "POST" and request.is_ajax():
        print("postPOSTPOSTPOST")
        post_id_cm = request.POST.get("post_id_cm")

        if post_id_cm:
            print(f"POST ID CM {post_id_cm}")
            text_coment = request.POST.get('text_comment')
            comment = models.CommentModel.objects.create(
                user=request.user,
                content=text_coment,
                post=models.PostModel.objects.filter(id=post_id_cm).last(),
            )
            return JsonResponse({
                'append': True,
                'image': comment.user.get_image(),
                'user': comment.user.username,
                'text_comment': text_coment,
                'count': post.commentmodel_set.all().count()

            })
    return render(request, 'shot-gallery-for-modal.html', context)


def explore_people(request):
    my_following= [follow.to_user for follow in request.user.following.all()]
    context['users']=User.objects.all().exclude(id=request.user.id)

    context["my_page"] = my_following

    if request.method == "POST" and request.is_ajax():
        user_id = request.POST.get("user_id")
        follow = models.FollowModel.objects.filter(
            from_user=request.user,
            to_user_id=user_id
        ).last()
        if not follow:
            models.FollowModel.objects.create(
                from_user=request.user,
                to_user_id=user_id
            )
            return JsonResponse({
                "status" : True
            })
        else:
            follow.delete()
            return JsonResponse({
                'status' : False
            })

    return render(request, 'explorepeople.html',context)

def user_followers(request):
    context['followers'] = [follow.from_user for follow in request.user.followers.all()]
    return render(request, 'user-followers.html',context)

def user_following(request):
    context["following"] = [follow.to_user for follow in request.user.following.all()]
    context['name'] = 'narmin'
    # return HttpResponse(request.user.following.all()[0].username)
    return render(request, 'user-following.html', context)


def social_settings(request):
    icons = request.user.usericon_set.filter(user=request.user)[0]

    context['form'] = forms.SocialForm(instance=icons)
    if request.method == "POST":
        form = forms.SocialForm(request.POST,instance=icons)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponse('valid')

    return render(request, 'setting-socials.html', context)