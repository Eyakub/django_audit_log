# from django.dispatch import receiver
# from easyaudit.models import RequestEvent
# from core.models import RequestEventExtra
# from django.db.models.signals import post_save
# from django.contrib.gis.geoip2 import GeoIP2
# from core.middleware import get_current_request


# @receiver(post_save, sender=RequestEvent)
# def add_extra_info(sender, instance, created, **kwargs):
#     print("add_extra_info==========")
#     if created:
#         request = get_current_request()
#         print("request==========", request)
#         user_agent = getattr(request, '_easy_user_agent', '') if request else ''
#         print("user_agent==========", user_agent)
#         country = ''
#         if request:
#             try:
#                 from django.contrib.gis.geoip2 import GeoIP2
#                 g = GeoIP2()
#                 country = g.country_name(request.META.get('REMOTE_ADDR', ''))
#             except Exception:
#                 country = ''
#         RequestEventExtra.objects.create(
#             request_event=instance,
#             country=country,
#             user_agent=user_agent
#         )
