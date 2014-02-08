from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseBadRequest,\
    HttpResponseRedirect
from django.views.generic.base import View
from authentication.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from lib.utils import RequestUtils
from django.contrib.auth import authenticate, login, logout
from authentication.exceptions import AuthenticationException
from django.contrib.auth.decorators import login_required

# Create your views here.

class RegisterView(View):
    def post(self, request, *args, **kwargs):
        data = RequestUtils.get_parameters(request)
        
        form = RegisterForm(data)
        if form.is_valid():
            user = User.objects.create_user(
                                             form.cleaned_data['username'], 
                                             form.cleaned_data['email'], 
                                             form.cleaned_data['password'],
                                             )
            if form.cleaned_data['first_name']:
                user.first_name = form.cleaned_data['first_name']
            if form.cleaned_data['last_name']:
                user.last_name = form.cleaned_data['last_name']
            user.save()
            return HttpResponse('user is created')
        else:
            return HttpResponseBadRequest(str(form.errors))
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('get for registering')
    
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('get for login')
    
    def post(self, request, *args, **kwargs):
        data = RequestUtils.get_parameters(request)
        form = LoginForm(data)
        try:
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponse('login valid')
                    else:
                        raise AuthenticationException('User is not active')
                else:
                    raise AuthenticationException('Can not authenticate user')
            else:
                print(form.errors)
                return HttpResponse('can not login')
        except User.DoesNotExist:
            return HttpResponse('can not login')

def logout_user(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect('/')
    
@login_required(login_url='/#/login')
def authenticated_page(request):
    context = {'user': request.user}
    return render(request, 'authenticated_page.html', context)