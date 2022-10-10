
from django.http import HttpResponse

# Create your views here.

def LandingInterface(request):
    return HttpResponse("This is Going to be final Product.")

def LoginInterface(request):
    return HttpResponse("this is the login page for the Admin")

def AdminDashboard(request):
    return HttpResponse("This is the Welcoming page for the Admin")

def FileUploadPage(request):
    return HttpResponse("where the admin uploads a file")

def UpdateProfile(request):
    return HttpResponse("update admins profile / Profile Management section")
