from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView
from django.views.generic import UpdateView, DeleteView, FormView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.contrib.auth.models import User
from .forms import ContactForm, ConfirmDeleteForm, BlankForm



# Create your views here.
def index(request):
    """ Index page """
    params = {}
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "Message sent successfully.")
            return redirect(reverse_lazy("index")+"?tab={}".format(request.POST.get("tab")))
    params["form"] = ContactForm
    params["tab"] = request.GET.get("tab")
    return render(request, "resume/index.html", params)

