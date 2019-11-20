import json

from django.shortcuts import render

from .models import Artist
from .repository import ArtistRepository

def artists(request):
    artists = ArtistRepository.get_artists()
    return render(request, 'app.html', {
        'page': 'artists',
        'title': 'Artists',
        'data': json.dumps(artists)
    })


def artist(request, id):
    artist = ArtistRepository.get_artist(id)
    return render(request, 'app.html', {
        'page': 'artist',
        'title': artist['name'],
        'data': json.dumps(artist)
    })
