from django.shortcuts import render_to_response, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView

# Create your views here.

# def has_permission(request):
#     return request.user.is_active #and request.user.is_staff

def login(request):
    #import pdb;pdb.set_trace()
    if request.user.is_superuser:
        return HttpResponseRedirect('/account/loggedin')
    else:
        c ={}
        c.update(csrf(request))
        return render_to_response('login.html',c)

def auth_view(request):

    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        if request.user.is_superuser:
            return HttpResponseRedirect('/account/loggedin')
        else:
        	return render_to_response('invaild_auth.html')
    else:
        return render_to_response('invalid_login.html')

def home(request):
    return render_to_response('base.html')

def loggedin(request):
    if not(request.user.is_superuser):
        return HttpResponseRedirect('/account/logout')
    return render_to_response('loggedin.html',{'full_name': ((request.user.first_name)+(request.user.last_name))})
    
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
