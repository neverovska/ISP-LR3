from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User


class Signin(TemplateView):
    template_name = 'user/signin.html'


class LoginView(TemplateView):
    template_name = "user/signin.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)


class RegisterView(TemplateView):
    template_name = "user/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect('/')

        return render(request, self.template_name)
