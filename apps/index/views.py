from django.shortcuts import render
from django.views import View
import logging

# Create your views here.
logger = logging.getLogger('django')

class Index(View):
    def get(self, request):
        return render(request, 'index/index.html')

class Register(View):
    def get(self, request):
        return render(request, 'index/register.html')

