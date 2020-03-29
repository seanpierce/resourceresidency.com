import json

from django.shortcuts import render

from .repository import ContentRepository

def about(request):
    events = ContentRepository.get_events()
    return render(request, 'app.html', {
        'page': 'about',
        'title': 'About RR',
        'data': json.dumps(events)
    })

def events(request):
    events = ContentRepository.get_events()
    return render(request, 'app.html', {
        'page': 'about',
        'title': 'About RR',
        'data': json.dumps(events)
    })
