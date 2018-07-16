from django.shortcuts import render
from .models import holding

# Create your views here.
def home(request):
    myholdings = holding.objects
    return render(request, 'holdings/home.html', {'myholdings':myholdings})
