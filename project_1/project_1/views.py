from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Home page")

def about (request):
    return HttpResponse("Hello About Page")