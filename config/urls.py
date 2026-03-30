"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from applications.views import register, JobApplicationListView, JobApplicationCreateView, JobApplicationUpdateView, \
    JobApplicationDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name="register"),
    path('applications/', JobApplicationListView.as_view(), name="application-list"),
    path('applications/create/', JobApplicationCreateView.as_view(), name="application-create"),
    path('applications/<int:pk>/update/', JobApplicationUpdateView.as_view(), name="application-update"),
    path('applications/<int:pk>/delete/', JobApplicationDeleteView.as_view(), name="application-delete"),

]
