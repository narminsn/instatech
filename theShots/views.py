from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import RegisterForm
from theShots.forms import UserCreationForm
from . import models
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from userApp.models import PostModel, LikeModel
from userApp.forms import Comment

from django.core.paginator import Paginator


# Create your views here.

def common_data():
    context = {
        'menu': models.MenuModel.objects.all(),
        'copy': models.CopyrightModel.objects.first(),
        'header': models.HeaderModel.objects.first(),
        "staff" : models.StaffPick.objects.first(),
        'offer' : models.OfferModel.objects.first(),
        'offer_sections' : models.OfferModel.objects.first().offersection_set.all(),
        'statistic' : models.StaticticsModel.objects.all(),
        'footer_text' : models.FooterText.objects.all(),
        'footer_url' : models.FooterUrls.objects.all(),
        'register_form' : UserCreationForm()

    }
    return context


def about_view(request):
    context = common_data()
    context['about'] = models.AboutModel.objects.first()
    context['about_team'] = models.AboutTeam.objects.first()
    context['team'] = models.TeamModel.objects.all()
    if request.method == "POST" and request.is_ajax():
        return HttpResponse('ajax')

    return render(request, 'page-about.html', context)


def verify_view(request, token, user_id):
    verify = models.VerificationModel.objects.filter(token=token, user_id=user_id,expire_date=False).last()
    if verify:
        verify.expire_date = True
        verify.save()
        verify.user.is_active = True
        verify.user.save()
        messages.info(
            request, "Success"
        )
        return HttpResponse("DFGHJK")
    else:
        return redirect('base-view')


def contact_view(request):
    return render(request, 'page-contact.html',context)

def explore_view(request):
    context = common_data()
    pagination = Paginator(PostModel.objects.all(), 4 )
    context["posts"] = pagination.get_page(request.GET.get('page', 1))
    context["page_range"] = pagination.page_range
    # context['posts'] = PostModel.objects.all()
    context['likes'] = [like.post for like in request.user.likemodel_set.all()]
    # if request.method == "POST" and request.is_ajax():
    #     # return HttpResponse("post")
    #     post_id = request.POST.get("post_id")
    #     post= PostModel.objects.filter(id=post_id).last()
    #     if post:
    #         print(post.title, post_id)
    #         like = LikeModel.objects.filter(post=post,user=request.user).last()
    #         if like:
    #
    #             post.like_count -= 1
    #             post.save()
    #             like.delete()
    #         else:
    #             if not post.like_count:
    #                 post.like_count = 1
    #             else:
    #                 post.like_count += 1
    #             post.save()
    #             LikeModel.objects.create(
    #                 user=request.user,
    #                 post=post
    #             )
    # if 'content' in request.POST:
    # if request.method == 'POST' and request.is_ajax():
    #     return HttpResponse('post')




    return render(request, 'explore-style1.html',context)


def input(request):
    if request.method == 'POST':
        return HttpResponse('post')
    return render(request,'input.html')

def fag_view(request):
    return  render(request, 'page-faq.html')