from .models import Content, Event, File

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

    @staticmethod
    def get_events():
        events = []
        
        for event in (Event.objects.order_by('-event_date')):
            events.append({
                'id': event.id,
                'name': event.name,
                'info': event.info,
                'files': list(File.objects.filter(event=event).values('event_file')),
            })

        return events