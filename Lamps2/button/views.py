from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from gpiozero import PWMLED 



from time import sleep 

led = PWMLED(5)
from tkinter import *
  


def home(request):
  # state = request.GET.get('mybtn')
  # if state:
  #   if state == "On": 
  #    if led.value == 0:
  #       led.value = 1
  #   elif led.value == 1:
  #     print("vliza")
  #     led.value = 0
  # with open("database.txt",r) as fd:
  #   file_contents = bool{fd.read()} or False

  return render(request,"home.html")