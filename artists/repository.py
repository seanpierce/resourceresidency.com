from .models import Artist

class ArtistRepository(object):
    """Access layer for artist data."""

    @staticmethod
    def get_artists():
        return list(Artist.objects
            .filter(active=True)
            .order_by('name')
            .values('id', 'name'))

    @staticmethod
    def get_artist(id):
        artist = Artist.objects.filter(active=True, id=id).first()
        return {
            'id': artist.id,
            'name': artist.name,
            'info': artist.info,
            'residencies': list(artist.residency_set.all()
                .values('id', 'name'))
        }