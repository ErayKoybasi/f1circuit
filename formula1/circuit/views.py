from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
  circuit = Circuit.objects.all()
  context = {
    'circuit' : circuit
  }
  return render(request, 'index.html', context)