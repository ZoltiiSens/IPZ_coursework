from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import todo_week_form, todo_todo_form
from .models import Week, Todo


@login_required
def week_list(request):
    form = todo_week_form()
    weeks_list_objects = Week.objects.filter(user=request.user, archived=False)
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


@login_required
def week_list_archive(request):
    weeks_list_objects = Week.objects.filter(user=request.user, archived=True)
    context = {'weeks_list': weeks_list_objects}
    if request.method == 'GET':
        return render(request, 'todo/week_archive.html', context)
    else:
        week_pk = request.POST['id']
        week = get_object_or_404(Week, pk=week_pk, user=request.user)
        week.archived = False
        week.save()
        return render(request, 'todo/week_archive.html', context)


@login_required
def week_show(request, week_pk):
    week = get_object_or_404(Week, pk=week_pk, user=request.user)
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


@login_required
def week_delete(request, week_pk):
    week = get_object_or_404(Week, pk=week_pk, user=request.user)
    if request.method == 'POST':
        week.delete()
        return redirect('week_list')


@login_required
def week_archive(request, week_pk):
    week = get_object_or_404(Week, pk=week_pk, user=request.user)
    if request.method == 'POST':
        week.archived = True
        week.save()
        return redirect('week_list')


@login_required
def create_todo(request, week_pk):
    week = get_object_or_404(Week, pk=week_pk, user=request.user)
    if request.method == "GET":
        return redirect('week_show', week_pk=week_pk)
    else:
        new_todo = Todo(title='', week_id=week.id)
        new_todo.save()
        return redirect('week_show', week_pk=week.id)


@login_required
def delete_todo(request, week_pk, todo_pk):
    week = get_object_or_404(Week, pk=week_pk, user=request.user)
    todo = get_object_or_404(Todo, pk=todo_pk, week_id=week.id)
    if request.method == "POST":
        todo.delete()
        return redirect('week_show', week_pk=week.id)
