from django.shortcuts import render, redirect, get_object_or_404
from .forms import todo_week_form, todo_todo_form
from .models import Week, Todo


def week_list(request):
    form = todo_week_form()
    weeks_list_objects = Week.objects.filter(user=request.user)
    context = {'form': form, 'weeks_list': weeks_list_objects}
    if request.method == 'GET':
        return render(request, 'todo/week_list.html', context)
    else:
        try:
            form = todo_week_form(request.POST)
            new_week = form.save(commit=False)
            new_week.user = request.user
            new_week.save()
            return render(request, 'todo/week_list.html', context)
        except ValueError:
            context['error'] = 'Bad data passed in. Try again'
            return render(request, 'todo/week_list.html', context)


def week_show(request, week_pk):
    week = get_object_or_404(Week, pk=week_pk)
    todo_list = Todo.objects.filter(week=week_pk)
    form = todo_todo_form()
    context = {'week': week, 'todo_list': todo_list, 'form': form}
    if request.method == 'GET':
        return render(request, 'todo/week_show.html', context=context)
    else:
        try:
            current_todo = get_object_or_404(Todo, pk=request.POST['id'])
            todo_changed = todo_todo_form(request.POST, instance=current_todo)
            todo_changed.save()
            return render(request, 'todo/week_show.html', context=context)
        except ValueError:
            context['error'] = 'Bad data'
            return render(request, 'todo/week_show.html', context=context)


def create_todo(request):
    week_pk = request.POST['week']
    if request.method == "GET":
        return redirect('week_show', week_pk=week_pk)
    else:
        new_todo = Todo(title='', week_id=week_pk)
        new_todo.save()
        return redirect('week_show', week_pk=week_pk)


def delete_todo(request):
    todo_id = request.POST['id']
    pass