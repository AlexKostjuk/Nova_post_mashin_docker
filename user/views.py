from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from user.forms import LoginForm, RegisterForm


# Create your views here.


class Login_View(View):

    def get(self, request):
        context = {}
        context['form'] = LoginForm()
        return render(request, 'login.html', context=context)
    def post(self, request):

        form = LoginForm(request.POST)
        context = {}
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/user/')
            context['error'] = 'invalid username or pasword'
            context['form'] = LoginForm()
            return render(request, 'login.html', context=context)


# def login_view (request):
#    context = {}
#    if request.method == 'POST':
#       form = LoginForm(request.POST)
#       if form.is_valid():
#          user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#          if user is not None:
#             login(request, user)
#             return redirect('/user/')
#       context['error'] = 'invalid username or pasword'
#    context['form'] = LoginForm()
#    return render(request, 'login.html', context=context)


def logout_view(request):
   logout(request)
   return redirect('/login/')


class Register_View(View):

    def get(self, request):
        return render(request, 'register.html', context={'form': RegisterForm()})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'],
                                            first_name=form.cleaned_data['fname'],
                                            last_name=form.cleaned_data['lname']
                                            )
            user.save()
            return redirect('/login/')



# def register_view(request):
#    if request.method == 'POST':
#       form = RegisterForm(request.POST)
#       if form.is_valid():
#
#          user = User.objects.create_user(username=form.cleaned_data['username'],
#                                          email=form.cleaned_data['email'],
#                                          password=form.cleaned_data['password'],
#                                          first_name=form.cleaned_data['fname'],
#                                          last_name=form.cleaned_data['lname']
#                                          )
#          user.save()
#          return redirect('/login/')
#    else:
#       return render(request, 'register.html',context={'form':RegisterForm()})


@login_required
def user_page (request):
   return render(request, 'user_page.html', context={'username' : request.user.username, 'email' : request.user.email})
