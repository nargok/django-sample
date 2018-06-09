# from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def hello(request):
    context = {'message': 'メッセージ'}
    return TemplateResponse(request, 'item/message.html', context=context)