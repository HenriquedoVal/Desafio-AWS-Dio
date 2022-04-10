from django.shortcuts import render
from core.models import Movie

# Create your views here.

def index(request):
    dados = Movie.objects.all()
    dados = {'movies': dados}
    return render(request, 'index.html', dados)