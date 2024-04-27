from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('Patinzrider - Home')

def about(request):
  return HttpResponse('Patinrzider - About')
