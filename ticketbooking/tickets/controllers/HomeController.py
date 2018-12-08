from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from tickets.models import Poster

class HomeController:

    def index(request):
        posters = Poster.objects.all()
        return render(request, 'pages/index.html', {'posters': posters})
