from django.shortcuts import render
from .models import Car
from django.core.paginator import Paginator


def index(request):
    size_const = 6
    all_car = Car.objects.all()

    paginator = Paginator(all_car, size_const)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/cars.html', context={
        'page_view': 'cars',
        'cars': page_obj
    })
