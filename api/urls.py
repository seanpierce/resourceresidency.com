from django.urls import path

from .content_api import GetEvents, GetContent

urlpatterns = [
    path('events', GetEvents.as_view()),
    path('content/<name>', GetContent.as_view())
]