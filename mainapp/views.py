from django.shortcuts import render
from django.http import HttpResponse
from .task import task_func

# Create your views here.
def test(request):
    task_func.delay()
    return HttpResponse("Done")