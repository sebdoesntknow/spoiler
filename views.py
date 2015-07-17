from random import randint
from django.shortcuts import render, get_object_or_404

from .models import Title, Spoiler

def index(request):
    title = get_object_or_404(Title, pk=randint(1, Title.objects.count()))
    spoiler_choices = [sp.id for sp in title.spoiler_set.all()]
    spoiler = title.spoiler_set.get(pk=spoiler_choices[randint(0, len(spoiler_choices) -1)])
    return render(request, 'web_spoiler/index.html',
                  {'title': title.title_text,
                   'spoiler': spoiler,
                   'dynamic_url': "Generate tinyurl link here",
                  })


def spoiler_detail(request, spoiler_id):
    requested_spoiler = Spoiler.objects.get(pk=spoiler_id)
    return render(request, 'web_spoiler/detail.html',
                  {'title': requested_spoiler.title.title_text,
                   'spoiler': requested_spoiler.spoiler_text,
                  })
