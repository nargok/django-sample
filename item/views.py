# from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def hello(request):
    context = {
      'headers': {
        'scheme': request.scheme,
        'path': request.path,
        'method': request.method,
        'content_length': request.META['CONTENT_LENGTH'],
        'http_accept': request.META['HTTP_ACCEPT'],
        'http_accept_language': request.META['HTTP_ACCEPT_LANGUAGE'],
        'user_agent': request.META['HTTP_USER_AGENT'],
        'remote_addr': request.META['REMOTE_ADDR'],    
      }
    }

    return TemplateResponse(request, 'item/header.html', context)