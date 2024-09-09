from django.shortcuts import render
from rest_framework.views import APIView
import requests
import logging

logger= logging.getLogger(__name__)


class HelloView(APIView):
        def get(self,request):
            try:
                logger.info('calling httpbin')
                response=requests.get('https://httpbin.org/delay/2')
                logger.info('received the response')
                data=response.json()
            except request.ConnectionError:
                 logger.critical('httpbin is offline')
            return render(request, 'hello.html', {'name':'Ahmad'})
                
