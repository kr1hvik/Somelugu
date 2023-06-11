from django.shortcuts import render
from .models import Question, Choice


def quiz(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, "t77lehed/quiz.html", context)

from .models import Quiz, Question

def submit_quiz(request):
    if request.method == 'POST':
        num_correct_answers = 0

        # Iterate through each question and compare the submitted answer with the correct choice
        for question in Question.objects.all():
            submitted_answer = request.POST.get(f'question{question.id}')
            try:
                choice = Choice.objects.get(id=int(submitted_answer), question=question)
                if choice.is_correct:
                    num_correct_answers += 1
            except Choice.DoesNotExist:
                pass

        context = {'num_correct_answers': num_correct_answers}

        return render(request, 't77lehed/results.html', context)

