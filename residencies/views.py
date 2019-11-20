import json

from django.shortcuts import render

from .models import Residency
from .repository import ResidencyRepository

def residencies(request):
    residencies = ResidencyRepository.get_residencies()
    return render(request, 'app.html', {
        'page': 'residencies',
        'title': 'Residencies',
        'data': json.dumps(residencies)
    })


def residency(request, id):
    residency = ResidencyRepository.get_residency(id)
    return render(request, 'app.html', {
        'page': 'residency',
        'title': residency['name'],
        'data': json.dumps(residency)
    })