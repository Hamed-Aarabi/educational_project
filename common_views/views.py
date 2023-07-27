from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import resolve
from account.models import MyUser


# Comment Section Codes
def comment_like(request, model):
    if model.likes.filter(id=request.user.id).exists():
        model.likes.remove(request.user.id)
        return JsonResponse({'response': 'remove_like'})
    else:
        model.likes.add(request.user.id)
        if model.dislikes.filter(id=request.user.id).exists():
            model.dislikes.remove(request.user.id)
        return JsonResponse({'response': 'like'})


def comment_dislike(request, model):
    if model.dislikes.filter(id=request.user.id).exists():
        model.dislikes.remove(request.user.id)
        return JsonResponse({'response': 'remove_dislike'})
    else:
        model.dislikes.add(request.user.id)
        if model.likes.filter(id=request.user.id).exists():
            model.likes.remove(request.user.id)
        return JsonResponse({'response': 'dislike'})


def comment_heart(request, model):
    if model.heart.filter(id=request.user.id).exists():
        model.heart.remove(request.user.id)
        return JsonResponse({'response': 'remove_heart'})
    else:
        model.heart.add(request.user.id)
        return JsonResponse({'response': 'heart'})


def comment_paginator(request, model):
    paginator = Paginator(model, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def get_app_name(request):
    match = resolve(request.path)
    app_name = match.app_name
    return app_name


# Get Data From Post Method For Create Comments
def create_comment(request):
    text = request.POST.get('text')
    parent = request.POST.get('reply_id', None)
    if request.user.is_authenticated:
        user = MyUser.objects.get(id=request.user.id)
        name, email = user, user.email
    else:
        name, email = request.POST.get('name'), request.POST.get('email')
    return name, email, parent, text
