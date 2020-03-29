from django.shortcuts import render

def index(request):
    """Default view for the application.
    """

    return render(request, 'app.html', {
        'page': 'home',
        'title': 'Home'
    })

def events(request):
    return render(request, 'app.html', {
        'page': 'events',
        'title': 'Events'
    })

def about(request):
    return render(request, 'app.html', {
        'page': 'about',
        'title': 'About'
    })