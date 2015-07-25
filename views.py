from django.shortcuts import render, get_object_or_404
from web_spoiler.spoiler_tools.tinyurl_tools import tinyurl_field_checker

from .models import Title, Spoiler

def index(request):
    spoiler = Spoiler.objects.order_by('?').first()
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

def titles_menu(request):
    titles_list = Title.objects.order_by('title_text')
    return render(request, 'web_spoiler/titles_menu.html',
                  {'titles_list': titles_list})

def single_title(request, title_id):
    title = get_object_or_404(Title, pk=title_id)
    title_spoiler = title.spoiler_set.order_by('?').first()
    return render(request, 'web_spoiler/title_spoiler.html',
                  {'title_spoiler': title_spoiler})
