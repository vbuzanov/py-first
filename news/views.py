from django.shortcuts import render
from .models import *

def index(request):
    context = {
        'news': New.objects.order_by('-published'),
    }
    return render(request, template_name='news/index.html', context=context)
