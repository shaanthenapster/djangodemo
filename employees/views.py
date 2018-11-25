from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> this is the beginning </h1> <p> hope you are enjoying")
