from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def foods(request):
  return HttpResponse('Patinzrider - Foods')

def food(request, food_id):
  return HttpResponse('Menu id =' + str(food_id) )