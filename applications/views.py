from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import JobApplication
from django.urls import reverse_lazy


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


class JobApplicationListView(ListView):
    model = JobApplication


class JobApplicationCreateView(CreateView):
    model = JobApplication
    fields = ["company_name", "job_title", "date_applied", "status", "notes"]
    success_url = reverse_lazy("application-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JobApplicationUpdateView(UpdateView):
    model = JobApplication
    fields = ["company_name", "job_title", "date_applied", "status", "notes"]
    success_url = reverse_lazy("application-list")


class JobApplicationDeleteView(DeleteView):
    model = JobApplication
    success_url = reverse_lazy("application-list")