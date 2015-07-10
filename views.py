from random import randint
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Title, Spoiler

def index(request):
    title = get_object_or_404(Title, pk=randint(1, Title.objects.count()))
    spoiler_choices = [sp.id for sp in title.spoiler_set.all()]
    spoiler = title.spoiler_set.get(pk=spoiler_choices[randint(0, len(spoiler_choices) -1)])
    
    return render(request, 'web_spoiler/index.html', {'title': title.title_text, 'spoiler': spoiler})


