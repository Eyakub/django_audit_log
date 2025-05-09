from django.utils.deprecation import MiddlewareMixin
from easyaudit.models import RequestEvent
from core.models import RequestEventExtra
from django.contrib.gis.geoip2 import GeoIP2


class XForwardedForMiddleware(MiddlewareMixin):
    """
    Middleware to handle X-Forwarded-For header for proper IP detection
    when behind a proxy (like Docker).
    """
    def process_request(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            request.META['REMOTE_ADDR'] = x_forwarded_for.split(',')[0].strip()


class RequestEventEnrichMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        try:
            # Find the latest RequestEvent for this user and IP
            user = request.user if request.user.is_authenticated else None
            remote_ip = request.META.get('REMOTE_ADDR', '')
            event = RequestEvent.objects.filter(user=user, remote_ip=remote_ip).order_by('-datetime').first()
            if event:
                user_agent = request.META.get('HTTP_USER_AGENT', '')
                country = ''
                try:
                    g = GeoIP2()
                    country = g.country_name('remote_ip')
                except Exception:
                    country = ''
                RequestEventExtra.objects.update_or_create(
                    request_event=event,
                    defaults={'country': country, 'user_agent': user_agent}
                )
        except Exception as e:
            print("Error in RequestEventEnrichMiddleware:", e)
        return response
