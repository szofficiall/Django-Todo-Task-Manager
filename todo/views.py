from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task


def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")

    return render(
        request,
        "todo/task_list.html",
        {"tasks": tasks}
    )


def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        if not title:
            messages.error(request, "Title cannot be empty.")

            return render(
                request,
                "todo/task_form.html",
                {
                    "title": title,
                    "description": description,
                }
            )

        Task.objects.create(
            title=title,
            description=description
        )

        messages.success(request, "Task created successfully.")

        return redirect("todo:task_list")

    return render(request, "todo/task_form.html")


def task_update(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        completed = request.POST.get("completed") == "on"

        if not title:
            messages.error(request, "Title cannot be empty.")

            return render(
                request,
                "todo/task_form.html",
                {"task": task}
            )

        task.title = title
        task.description = description
        task.completed = completed
        task.save()

        messages.success(request, "Task updated successfully.")

        return redirect("todo:task_list")

    return render(
        request,
        "todo/task_form.html",
        {"task": task}
    )


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.delete()

        messages.success(request, "Task deleted successfully.")

        return redirect("todo:task_list")

    return render(
        request,
        "todo/task_confirm_delete.html",
        {"task": task}
    )


def task_toggle_complete(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.completed = not task.completed
        task.save()

        if task.completed:
            messages.success(request, "Task marked as completed.")
        else:
            messages.info(request, "Task marked as pending.")

    return redirect("todo:task_list")