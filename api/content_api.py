import json

from django.http import HttpResponse
from django.views.generic import View

from content.repository import ContentRepository as repo

class GetContent(View):
    """
    Gets 'Content' data by name.
    """
    def get(self, request, *args, **kwargs):
        name = self.kwargs['name']
        return HttpResponse(json.dumps(repo.get_content_by_name(name)), content_type="application/json")

class GetEvents(View):
    """
    Returns 'Event' data.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(repo.get_events()), content_type="application/json")