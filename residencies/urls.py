from django.urls import path

from .views import residencies, residency

urlpatterns = [
    path('', residencies),
    path('<id>', residency),
]