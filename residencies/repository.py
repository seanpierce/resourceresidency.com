from django.core import serializers

from .models import Residency

class ResidencyRepository(object):
    """Access layer for residency data."""

    @staticmethod
    def get_residencies():
        return list(Residency.objects
            .filter(active=True)
            .order_by('name')
            .values('id', 'name'))

    @staticmethod
    def get_residency(id):
        residency = Residency.objects.filter(active=True, id=id).first()
        return {
            'id': residency.id,
            'name': residency.name,
            'info': residency.info,
            'artists': list(residency.artists.all()
                .values('id', 'name'))
        }
