from django.shortcuts import render,redirect
from .forms import formInput
import time


def input_view(request):
    if request.method == 'POST':
        form = formInput(request.POST)
        if form.is_valid():
            request.session["duration"] = form.cleaned_data["duration"]
            request.session["interval"] = form.cleaned_data["interval"]
            request.session["msg"] = form.cleaned_data["msg"]
            return redirect("result")

    form = formInput()
    return render(request,"core/index.html",{"form" : form})

def result_view(request):
    return render(request, "core/result.html", {
        "duration": request.session.get("duration"),
        "interval": request.session.get("interval"),
        "msg": request.session.get("msg"),
    })

def reset_session(request):
    request.session.flush()  # ⬅️ HAPUS SEMUA SESSION
    return redirect("home")
        