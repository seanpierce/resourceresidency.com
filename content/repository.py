from .models import Content

class ContentRepository(object):
    """Access layer for content data."""

    @staticmethod
    def get_content_by_name(name):
        content = Content.objects.filter(active=True, name=name).first()
        return {
            'id': content.id,
            'name': content.name,
            'info': content.info
        }