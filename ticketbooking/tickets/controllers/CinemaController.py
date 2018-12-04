from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

class CinemaController:

    def test(request):
        return render(request, 'pages/test.html', {})
