from django.urls import path

from .views import artists, artist

urlpatterns = [
    path('', artists),
    path('<id>', artist),
]