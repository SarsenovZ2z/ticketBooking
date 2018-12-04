from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

class HomeController:

    def index(request):
        return render(request, 'pages/index.html', {})
