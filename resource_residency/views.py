from django.shortcuts import render

def index(request):
    """Default view for the application.
    """

    return render(request, 'app.html')