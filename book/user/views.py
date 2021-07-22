from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy


# Create your views here.


class UserLoginView(LoginView):
    template_name = "user/login.html"

    # success_url = reverse_lazy('creat-phone')
    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(LogoutView):
    def get_next_page(self):
        return reverse_lazy('home')
