from django.shortcuts import render


def week_list(request):
    return render(request, 'todo/week_list.html')
