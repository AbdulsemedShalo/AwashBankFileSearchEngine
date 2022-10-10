
from django.http import HttpResponse

# Create your views here.

def LoginInterface(request):
    return HttpResponse("this is the login page for the Admin")

def FileUploadPage(request):
    return HttpResponse("where the admin uploads a file")

