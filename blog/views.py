from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import blog
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
from authentication.models import profile

@login_required
def blogs(request, slug):
    user = request.user
    data1 = blog.objects.filter(topic=slug)
    usr = request.user
    prf = profile.objects.get(user = usr)
    data = {
        'user_id': usr.username,
        'name': prf.name,
        'picture': prf.image,
        'email': prf.email,
        'datas': data1,
    }
    return render(request, 'blog.html', data)


@login_required
def new_blog(request):
    user = request.user
    if(request.method == 'POST'):
        ttle = request.POST.get('title')
        dcx = request.POST.get('description')
        tpc = request.POST.get('topic')
        temp = blog()
        temp.author = user
        temp.title = ttle
        temp.content = dcx
        temp.catagory = tpc
        temp.save()
        return redirect('/blog')
    usr = request.user
    prof = profile.objects.get(user = usr)
    data = {
        'user_id': usr.username,
        'name': prof.name,
        'picture': prof.image,
        'email': prof.email,
    }
    return render(request, 'new_blog.html', data)


@csrf_exempt
def like(request):
    if request.is_ajax():
        message = "success"
        dta = request.POST.get('post_id')
        data = blog.objects.get(id=dta)
        data.likes += 1
        data.save()
        #print(dta, " Yes")
        return HttpResponse(message)
    else:
        print('no')


@login_required
def user_blog(request, slug):
    usr = User.objects.get(username=slug)
    print(usr)
    data = blog.objects.filter(author=usr)
    prof = profile.objects.get(user = usr)
    print(usr.first_name)
    datas = {
        'user_id': usr.username,
        'name': prof.name,
        'picture': prof.image,
        'email': prof.email,
    }
    context = {
        'datas': data,
        'usr': datas
    }
    return render(request, 'blog.html', context)


@login_required
def all_blogs(request):
    data = blog.objects.all()
    prf = profile.objects.get(user = request.user)
    context = {
        'datas': data,
        'prof':prf
    }

    return render(request, 'blog.html', context=context)


def my_blogs(request):
    user = request.user
    data = blog.objects.filter(author=user)
    context = {
        'datas': data,
        'my': True
    }
    return render(request, 'blog.html', context=context)