from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html')
    elif request.method == 'POST':
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

        user = User.objects.create_user(login_x, email_x, pass1_x)
        if user is None:
            return render(request, 'account/report.html')
        else:
            user.save()
            return render(request, 'account/success.html')


def entry(request):
    if request.method == 'GET':
        return render(request, 'account/entry.html')
    elif request.method == 'POST':
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')

        # 2 - Перевірка правдивості логіна і пароля...
        user = authenticate(request, username=login_x, password=pass1_x)
        if user is None:
            mess = 'Такого логіна незнайдено!'
            color = 'red'
            return render(request, 'account/report.html')
        else:
            login(request, user)
            return redirect('/')


def sign_out(request):
    logout(request)
    return render(request, 'account/logout.html')

"""
def ajax_reg(request):
    response = dict()
    login_y = request.GET.get('login')
    try:
        User.objects.get(username=login_y)
        response['message'] = 'занятий'
    except User.DoesnotExist:
        response['message'] = 'вільний'
    return JsonResponse(response)
"""