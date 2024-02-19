from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def condition(request):
    context = {
        'python' : False,
        'java' : True,
    }
    return render(request, 'condition.html', context)


def looping(request):
    context = {
        'cardContent': [['Beginner', 'Discussing the basics of Django framework.'], 
                        ['Intermediate', 'Exploring intermediate-level Django concepts.'], 
                        ['Advance', 'Advanced techniques and best practices in Django development.'], 
                        ['Expert','Expert-level tips and tricks for optimizing Django applications.']]
    }
    return render(request, 'looping.html', context)