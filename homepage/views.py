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
    question1 = Question.objects.create(text='Millist nime kandis Tallinna Reaalkool aastatel 1881-1890')
    Choice.objects.create(question=question1, text='Tallinna Peetri Reaalkool')
    Choice.objects.create(question=question1, text='Tallinna 2.Keskkool')
    Choice.objects.create(question=question1, text='Revalskoje Petrovskoje Realnoje Utšilštše')
    Choice.objects.create(question=question1, text='Tallinna Reaalkool')
    

    question2 = Question.objects.create(text='Kes oli esimene eestlasest direktor?')
    Choice.objects.create(question=question2, text='Peter Osse')
    Choice.objects.create(question=question2, text='Ernst Peterson Särgava')
    Choice.objects.create(question=question2, text='Nikolai Kann')
    Choice.objects.create(question=question2, text='Karl Koljo')
    Choice.objects.create(question=question2, text='Wilhelm Petersen')

    question3 = Question.objects.create(text='Kes kujundas Reaalkooli mütsi?')
    Choice.objects.create(question=question3, text='Roman Nyman')
    Choice.objects.create(question=question3, text='Nikolai Kann')
    Choice.objects.create(question=question3, text='Karl Koljo')
    Choice.objects.create(question=question3, text='Voldemar Resev-Resel')

    question4 = Question.objects.create(text='Mis aastast töötab Tallinna Reaalkoolis Ene Saar?')
    Choice.objects.create(question=question4, text='2004')
    Choice.objects.create(question=question4, text='2014')
    Choice.objects.create(question=question4, text='2010')
    Choice.objects.create(question=question4, text='2000')

    question5 = Question.objects.create(text='Kelle hüüdnimi oli "Pudi"?')
    Choice.objects.create(question=question5, text='Peter Osse')
    Choice.objects.create(question=question5, text='Paul Ederberg')
    Choice.objects.create(question=question5, text='Aleksei Tsõgankov')
    Choice.objects.create(question=question5, text='Voldemar Toomingas')

    question6 = Question.objects.create(text='Mis kuupäeval toimus uue maja pidulik avaaktus?')
    Choice.objects.create(question=question6, text='17.jaanuar 1884')
    Choice.objects.create(question=question6, text='13.november 1927')
    Choice.objects.create(question=question6, text='29.september 1881')

    question7 = Question.objects.create(text='Mis aastast pärineb esimene sõrmus?')
    Choice.objects.create(question=question7, text='1934')
    Choice.objects.create(question=question7, text='1939')
    Choice.objects.create(question=question7, text='1918')
    Choice.objects.create(question=question7, text='1916')

    question8 = Question.objects.create(text='Kellega seostatakse Reaali I kuldajastut?')
    Choice.objects.create(question=question8, text='Nikolai Kann')
    Choice.objects.create(question=question8, text='Ernst Peterson Särgava')
    Choice.objects.create(question=question8, text='Karl Koljo')
    Choice.objects.create(question=question8, text='Wilhelm Petersen')

    question9 = Question.objects.create(text='Mis kuupäeval eemaldati poiss esimest korda?')
    Choice.objects.create(question=question9, text='16.okoober 1948')
    Choice.objects.create(question=question9, text='29.märts 1948')
    Choice.objects.create(question=question9, text='28.august 1941')
    Choice.objects.create(question=question9, text='23.september 1940')

    question10 = Question.objects.create(text='Milline direktor lõi lõpukella traditsiooni?')
    Choice.objects.create(question=question10, text='Aleksei Tsõgankov')
    Choice.objects.create(question=question10, text='Mart Kuurme')
    Choice.objects.create(question=question10, text='Hain Hiieaas')
    Choice.objects.create(question=question10, text='Emilie Pertels')








from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Question, Choice, Answer

def submit_exam(request):
    if request.method == 'POST':
        questions = Question.objects.all()
        total_questions = len(questions)
        score = 0

        for question in questions:
            submitted_choices = request.POST.getlist(f"question_{question.id}_choice")
            correct_choices = [choice.id for choice in question.choice_set.filter(is_correct=True)]

            if submitted_choices == correct_choices:
                score += 1

            answer = Answer.objects.create(question=question)
            answer.choices.set(submitted_choices)

        percentage_score = (score / total_questions) * 100

        messages.success(request, f"Your score: {score}/{total_questions} ({percentage_score:.2f}%)")
        
        # Hardcoding the correct choices
        for question in questions:
            choices = question.choice_set.all()
            if question.text == 'Millist nime kandis Tallinna Reaalkool aastatel 1881-1890':
                choices[0].is_correct = True
            elif question.text == 'Kes oli esimene eestlasest direktor?':
                choices[1].is_correct = True
            elif question.text == 'Kes kujundas Reaalkooli mütsi?':
                choices[0].is_correct = True
            elif question.text == 'Mis aastast töötab Tallinna Reaalkoolis Ene Saar?':
                choices[2].is_correct = True
            elif question.text == 'Kelle hüüdnimi oli "Pudi"?':
                choices[1].is_correct = True
            elif question.text == 'Mis kuupäeval toimus uue maja pidulik avaaktus?':
                choices[0].is_correct = True
            elif question.text == 'Mis aastast pärineb esimene sõrmus?':
                choices[0].is_correct = True
            elif question.text == 'Kellega seostatakse Reaali I kuldajastut?':
                choices[0].is_correct = True
            elif question.text == 'Mis kuupäeval eemaldati poiss esimest korda?':
                choices[2].is_correct = True
            elif question.text == 'Milline direktor lõi lõpukella traditsiooni?':
                choices[3].is_correct = True
            
            # Save the changes for each question's choices
            for choice in choices:
                choice.save()
        
        return redirect('exam')
