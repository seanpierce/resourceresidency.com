from datetime import datetime, timedelta

from .models import Content, Event, File

class ContentRepository(object):
    """Access layer for content data."""

    @staticmethod
    def get_content_by_name(name):
        content = Content.objects.filter(active=True, name__iexact=name).first()
        return {
            'id': content.id,
            'name': content.name,
            'info': content.info
        }

    @staticmethod
    def get_events():
        """
        Returns event info, including the associated files and whether or not it has already ocurred.
        """
        now = datetime.now()
        events = []
        
        for event in (Event.objects.order_by('-event_date')):
            events.append({
                'id': event.id,
                'date': event.event_date.strftime("%m/%d/%Y"),
                'name': event.name,
                'info': event.info,
                'files': list(File.objects.filter(event=event).values('event_file')),
                'past': (event.event_date + timedelta(days=1)) < now.date()
            })

        return events