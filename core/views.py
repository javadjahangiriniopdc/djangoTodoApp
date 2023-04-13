from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from core.models import TODO
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'core/todo.html')


def todo_list(request):
    todos = TODO.objects.all()
    return JsonResponse({'todos': list(todos.values())})


@csrf_exempt
def todo_create(request):
    if request.method == 'POST':
        todo_name = request.POST.get('todo_name')
        todo = TODO.objects.filter(name=todo_name)
        if todo.exists():
            return JsonResponse({'status': 'error'})
        todo = TODO.objects.create(name=todo_name)
    return JsonResponse({'todo_name': todo_name, 'status': 'created'})


@csrf_exempt
def todo_edit(request):
    if request.method == "POST":
        todo_name = request.POST.get('todo_name')
        todo_name_new = request.POST.get('todo_name_new')
        completed = request.POST.get('completed')
        # search in database
        edited_todo = TODO.objects.get(name=todo_name)

        print(todo_name, completed)
        if completed:
            if completed == '0':
                edited_todo.completed = False
                edited_todo.save()
                return JsonResponse({'status': 'updated'})
            elif completed == '1':
                edited_todo.completed = True
                edited_todo.save()
                return JsonResponse({'status': 'updated'})

        if TODO.objects.filter(name=todo_name_new).exists():
            return JsonResponse({'status': 'error'})

        edited_todo.name = todo_name_new
        edited_todo.save()
        context = {'todo_name_new': todo_name_new,
                   'status': 'updated'}

    return JsonResponse(context)


@csrf_exempt
def todo_delete(request):
    if request.method == "POST":
        todo_name = request.POST.get('todo_name')
        TODO.objects.filter(name=todo_name).delete()
    return JsonResponse({'status': 'deleted'})
