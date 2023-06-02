from django.shortcuts import render

def home(response):
    return render(response, "homepage/main.html", {}) 
def realica(request):
    return render(request, "homepage/realica.html")


from .models import Question

def exam(request):
    questions = Question.objects.all()
    return render(request, 'homepage/exam.html', {'questions': questions})

def submit_exam(request):
    if request.method == 'POST':
        # Process the submitted answers
        # Calculate the score
        # Display the result
        pass

from homepage.models import Question, Choice
if not Question.objects.exists():
    question1 = Question.objects.create(text='Millist nime kandis Tallinna Reaalkool aastatel ...')
    Choice.objects.create(question=question1, text='Tallinna Peetri Reaalkool')
    Choice.objects.create(question=question1, text='Tallinna 2.Keskkool')
    Choice.objects.create(question=question1, text='54')
    Choice.objects.create(question=question1, text='Ma64drid')
    Choice.objects.create(question=question1, text='Ber46lin')
    

    question2 = Question.objects.create(text='What is the capital of France?')
    Choice.objects.create(question=question2, text='Paris')
    Choice.objects.create(question=question2, text='London')
    Choice.objects.create(question=question2, text='Berlin')
    Choice.objects.create(question=question2, text='Madrid')
    Choice.objects.create(question=question2, text='Berlin')

    question3 = Question.objects.create(text='Kes oli Pariisis?')
    Choice.objects.create(question=question3, text='Jamal')
    Choice.objects.create(question=question3, text='Austria kunstnik')
    Choice.objects.create(question=question3, text='Kanye')
    Choice.objects.create(question=question3, text='NIG')
    
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Question, Choice, Answer

def submit_exam(request):
    if request.method == 'POST':
        questions = Question.objects.all()
        total_questions = len(questions)
        score = 0

        for question in questions:
            # Get the submitted choices for each question
            submitted_choices = request.POST.getlist(f"question_{question.id}_choice")

            # Get the correct choices for the question
            correct_choices = [choice.id for choice in question.choice_set.filter(is_correct=True)]

            # Check if the submitted choices match the correct choices
            if submitted_choices == correct_choices:
                score += 1

            # Save the submitted answers for each question
            answer = Answer.objects.create(question=question)
            answer.choices.set(submitted_choices)

        # Calculate the percentage score
        percentage_score = (score / total_questions) * 100

        # Display the result
        messages.success(request, f"Your score: {score}/{total_questions} ({percentage_score:.2f}%)")

        return redirect('exam')