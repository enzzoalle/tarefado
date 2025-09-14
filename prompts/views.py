from django.shortcuts import render, redirect, get_object_or_404
from app.models import Prompt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from app.forms import PromptForm

@login_required(login_url="login_view")
def prompts(request):
    form = PromptForm()
    if request.method == "POST":
        form = PromptForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("prompts")
    itens = Prompt.objects.filter(user=request.user)
    return render(request, "prompts/prompts.html", {"form": form, "prompts": itens})

@login_required(login_url="login_view")
def prompt_edit(request, pk):
    obj = get_object_or_404(Prompt, pk=pk)
    if obj.user != request.user:
        return HttpResponseForbidden()
    if request.method == "POST":
        form = PromptForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("prompts")
    else:
        form = PromptForm(instance=obj)
    return render(request, "prompts/prompt_edit.html", {"form": form, "prompt": obj})

@login_required(login_url="login_view")
def prompt_delete(request, pk):
    obj = get_object_or_404(Prompt, pk=pk)
    if obj.user != request.user:
        return HttpResponseForbidden()
    if request.method == "POST":
        obj.delete()
        return redirect("prompts")
    return render(request, "prompts/prompt_delete_confirm.html", {"prompt": obj})