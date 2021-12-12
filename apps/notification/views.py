from django.shortcuts import render
from django.views import View
import logging
from notification.models import Notification
# Create your views here.

logger = logging.getLogger('django')
class NotificationGet(View):

    def get(self, request):
        notifications = Notification.objects.filter(is_delete=False)[:4]
        content_dict = {
            "notifications": notifications
        }
        return render(request, 'message/newslistpic.html', context=content_dict)