from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


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