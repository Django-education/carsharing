from django.shortcuts import render
from django.core.mail import send_mail
from .models import UserEmail, Feedback, Mailing


def index(request):
    return render(request, 'home/index.html')


def account(request):
    return render(request, 'home/account.html')


def cars(request):
    return render(request, 'home/cars.html')


def contacts(request):
    if request.method == 'GET':
        return render(request, 'home/contacts.html')
    elif request.method == 'POST':
        feedback = Feedback()
        feedback.first_name = request.POST.get('first_name')
        feedback.second_name = request.POST.get('second_name')
        feedback.user_email = request.POST.get('email')
        feedback.message = request.POST.get('message')
        feedback.save()

        site_response = 'Ваше повідомлення отримано і буде опрацьоване на протязі дня...'
        result = send_mail(feedback.user_email, site_response, 'MySite', [feedback.user_email], fail_silently=False)

        if result == 0:
            return render(request, 'account/report.html')
        elif result == 1:
            return render(request, 'contacts/success.html')
    """if request.method == 'GET':
        return render(request, 'home/newsletter.html')
    elif request.method == 'POST':
        target_email = request.POST.get('email')
        message_body = 
            Hello, dear User!

            You have subscribe to the newsletter
            from MySite
            We are open 24/7!
            You are contact our support 24/7!

            We will be glad to be of service to you!
            Come back more often!
        """


def information(request):
    return render(request, 'home/information.html')


def region(request):
    return render(request, 'home/region.html')


def tariffs(request):
    return render(request, 'home/tariffs.html')
