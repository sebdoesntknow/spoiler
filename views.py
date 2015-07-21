from random import randint
from django.shortcuts import render, get_object_or_404
from web_spoiler.spoiler_tools.tinyurl_tools import tinyurl_field_checker

from .models import Title, Spoiler

def index(request):
    spoiler = Spoiler.objects.all()[randint(0, Spoiler.objects.count() -1)]
    spoiler_title = get_object_or_404(Title, pk=spoiler.title_id)
    # Update tinyurl value for those that don't match the url
    tinyurl_field_checker(spoiler.pk)
    return render(request, 'web_spoiler/index.html',
                  {'title': spoiler_title.title_text,
                   'spoiler': spoiler.spoiler_text,
                   'dynamic_url': spoiler.tinyurl,
                  })

def spoiler_detail(request, spoiler_id):
    requested_spoiler = get_object_or_404(Spoiler, pk=spoiler_id)
    return render(request, 'web_spoiler/detail.html',
                  {'title': requested_spoiler.title.title_text,
                   'spoiler': requested_spoiler.spoiler_text,
                  })
