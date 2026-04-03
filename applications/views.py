from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import JobApplication
from django.urls import reverse_lazy
from .forms import JobApplicationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        # handle form submission
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request,
                          "registration/register.html",
                          context={"form": form})

    else:
        # show empty form
        return render(request,
               template_name="registration/register.html",
               context={"form": UserCreationForm()}
              )


class JobApplicationListView(LoginRequiredMixin, ListView):
    model = JobApplication

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

class JobApplicationCreateView(LoginRequiredMixin, CreateView):
    form_class = JobApplicationForm
    model = JobApplication
    success_url = reverse_lazy("application-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JobApplicationUpdateView(LoginRequiredMixin, UpdateView):
    form_class = JobApplicationForm
    model = JobApplication
    success_url = reverse_lazy("application-list")

    def get_object(self):
        return get_object_or_404(JobApplication, pk=self.kwargs["pk"], user=self.request.user)


class JobApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = JobApplication
    success_url = reverse_lazy("application-list")

    def get_object(self):
        return get_object_or_404(JobApplication, pk=self.kwargs["pk"], user=self.request.user)
