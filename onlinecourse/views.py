from django.shortcuts import render, redirect
from .models import Question, Choice, Submission

def submit(request):
    return redirect('show_exam_result')

def show_exam_result(request):
    context = {
        'score': 3,
        'total': 5,
    }
    return render(request, 'onlinecourse/result.html', context)