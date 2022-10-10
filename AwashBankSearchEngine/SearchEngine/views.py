
from django.http import HttpResponse

# Create your views here.

def loginInterface(request):
    return HttpResponse("this is the login page for the Employeers")

def fileUploadPage(request):
    return HttpResponse("where the admin uploads a file")

