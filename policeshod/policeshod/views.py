from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
import models
from django.shortcuts import render


def landing(request):
    content = {"P":"Police"}
    return render(request, 'main_page.html', content)
