from django.shortcuts import render_to_response
from .models import TestPermission

from django.views import generic
from django.template import RequestContext
from django.contrib.auth import authenticate, login

# Login screen
class LoginIndex(generic.TemplateView):
    template_name = 'login/login.html'

#def loginIndex(request):
#    return HttpResponse("Placeholder text")

# Test for submitting login
class HomePage(generic.TemplateView):
    template_name = 'login/home.html'

# Handling for retrieving the username and password

# For time reasons, users are currently being created manually by CDing to the manage.py file and running the
# below code in 'python manage.py shell'. Consider an interface to add users a TODO, since this would require
# permissions to create and manage users, GUI design, and other work there is not time for.

# from django.contrib.auth.models import User
# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
# user.save()

def getCredentials(request):
    # Define the test string
    displayString = ''

    # Grab the username and password here from the forms
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Authenticate using the premade django method
    usertoken = authenticate(username=username, password=password)

    # Basic authentication stuff
    if usertoken is None:
        displayString = 'Invalid username or password'

        # Bad credentials given; pack up and go to error string
        # TODO: if this gets used in mainstream production, move the display call to its own method
        credDict = {'displayString': displayString}
        return render_to_response('login/home.html',
                                  credDict,
                                  context_instance=RequestContext(request))
    else:
        # Login must be called after authenticating or will raise an error. Pretty sure that this allows
        # the user to be grabbed from the 'request' object as well
        login(request, usertoken)

        # Parrot back the user password from the text fields. Django encodes these in the User class and makes them
        # unobtainable for security reasons (might be able to get the username but couldn't find how).
        displayString = 'Successfully logged in with a username of "%s" and a password of "%s"' % (username, password)

    # Check for custom arbitrary permission
    if usertoken.has_perm('login.can_see'):
        displayString += "\n\nUser has permission to see this arbitrary text: ABC123"
    else:
        displayString += "\n\nUser does not have permission to see arbitrary text"

    # Pack display string into a dict and pass method. Probably a cleaner way to do this!
    credDict = {'displayString': displayString}
    return render_to_response('login/home.html',
                              credDict,
                              context_instance=RequestContext(request))