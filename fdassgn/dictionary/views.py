from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_POST
import re
from dictionary.forms import LongURL
from dictionary.models import DictWord


CLEANER = re.compile(r'[^0-9a-z/\.]')
SPLITTER = re.compile(r'[/\.]')


def home(request):
    form = LongURL()
    return render_to_response('home.html', RequestContext(request, {
        'form': form,
    }))


def _get_candidates(url):
    cleaned = CLEANER.sub('', (str(url)).lower())
    unique = list(set(SPLITTER.split(cleaned)))
    if '' in unique:
        unique.remove('')
    return unique


@require_POST
def create_short(request):
    form = LongURL(request.POST)
    if form.is_valid():
        long_url = form.data['url']
        try:
            word = DictWord.objects.get(URL=long_url)
        except ObjectDoesNotExist:
            pass
        else:
            word.ts = datetime.now()
            word.save()
            return HttpResponse('Already attached to: %s' % word.word)
        candidates = _get_candidates(long_url)
        words = DictWord.objects.filter(word__in=candidates).exclude(URL__isnull=False)
        if len(words) > 0:
            elig_word = words[0]
            elig_word.URL = long_url
            elig_word.ts = datetime.now()
            elig_word.save()
        else:
            empty_words = DictWord.objects.filter(URL__isnull=True)
            if len(empty_words) > 0:
                elig_word = empty_words[0]
                elig_word.URL = long_url
                elig_word.ts = datetime.now()
                elig_word.save()
            else:
                # fetch oldest and set it.
                pass
        return HttpResponse('Attached it to word: %s' % elig_word)
    else:
        return HttpResponse('URL is not valid')