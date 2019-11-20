import json

from django.shortcuts import render

from .repository import ContentRepository

def about(request):
    content = ContentRepository.get_content_by_name('About')
    return render(request, 'app.html', {
        'page': 'about',
        'title': 'About RR',
        'data': json.dumps(content)
    })
