from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Login screen
class LoginIndex(generic.TemplateView):
    template_name = 'login/login.html'

#def loginIndex(request):
#    return HttpResponse("Placeholder text")

# Test for submitting login
class HomePage(generic.TemplateView):
    template_name = 'login/home.html'

# Handling for retrieving the username and password
def getCredentials(request):
    return