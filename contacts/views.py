from django.shortcuts import render


def success(request):
    return render(request, 'contacts/success.html')
