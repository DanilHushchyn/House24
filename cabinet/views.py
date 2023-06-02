from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def statistic(request):
    return render(request, 'cabinet/statistic.html')


def profile(request):
    return render(request, 'cabinet/profile.html')