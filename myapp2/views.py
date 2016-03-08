from django.shortcuts import render_to_response, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView

# Create your views here.


def login(request):
    if request.user.is_active:
        return HttpResponseRedirect('/app2/loggedin')
    else:
        c ={}
        c.update(csrf(request))
        return render_to_response('login1.html',c)

def auth_view(request):

    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/app2/loggedin')
    else:
        return HttpResponseRedirect('/app2/invalid')

def loggedin(request):
    if not(request.user.is_active):
        return HttpResponseRedirect('/app2/logout')
    return render_to_response('loggedin1.html',{'full_name': ((request.user.first_name)+(request.user.last_name))})
    
    
def invalid_login(request):
    return render_to_response('invalid_login1.html')
    
def logout(request):
    auth.logout(request)
    return render_to_response('logout1.html')