from django.core import serializers

from .models import Artist

class ArtistRepository(object):
    """Access layer for artist data."""

    @staticmethod
    def get_artists():
        return list(Artist.objects            
            .filter(active=True)
            .order_by('name')
            .values('id', 'name', 'info'))

    @staticmethod
    def get_artist(id):
        artist = Artist.objects.filter(active=True, id=id).first()
        return {
            'id': artist.id,
            'name': artist.name,
            'info': artist.info
        }