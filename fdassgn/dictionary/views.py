from datetime import datetime
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import require_POST
import re
from dictionary.forms import LongURL
from dictionary.models import DictWord


CLEANER = re.compile(r'[^0-9a-z/\.\-]')
SPLITTER = re.compile(r'[/\.\-]')


def _get_candidates(url):
    cleaned = CLEANER.sub('', (str(url)).lower())
    unique = list(set(SPLITTER.split(cleaned)))
    if '' in unique:
        unique.remove('')
    return unique


def home(request):
    if request.method == 'GET':
        form = LongURL()
        return render_to_response('home.html', RequestContext(request, {
            'form': form,
        }))
    elif request.method == 'POST':
        form = LongURL(request.POST)
        if form.is_valid():
            long_url = form.data['url']
            try:
                word = DictWord.objects.get(URL=long_url)
            except ObjectDoesNotExist:
                print('This URL has not yet been assigned')
                # pass
            else:
                print('Already assigned')
                word.ts = datetime.now()
                word.save()
                messages.success(request, 'URL: %s/%s' % (request.META['HTTP_HOST'], word.word,))
                return HttpResponseRedirect(reverse('home'))

            candidates = _get_candidates(long_url)
            print('Candidate Words: %s' % str(candidates))
            words = DictWord.objects.filter(word__in=candidates).exclude(URL__isnull=False)
            if len(words) > 0:
                elig_word = words[0]
                print('Found some eligible words. Using: %s' % elig_word.word)
                elig_word.set_url(long_url)
            else:
                empty_words = DictWord.objects.filter(URL__isnull=True)
                if len(empty_words) > 0:
                    elig_word = empty_words[0]
                    print('Found no eligible word. Using: %s' % elig_word.word)
                    elig_word.set_url(long_url)
                else:
                    elig_word = DictWord.objects.all().order_by('ts')[0]
                    print('Run out. Reusing: %s' % elig_word.word)
                    elig_word.set_url(long_url)

            messages.success(request, 'URL: %s/%s' % (request.META['HTTP_HOST'], elig_word.word))
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('URL is not valid')


def redirection(request, r_word):
    selected_word = get_object_or_404(DictWord, word=r_word)
    if selected_word.URL is None:
        print(selected_word.URL)
        raise Http404
    else:
        return HttpResponseRedirect(selected_word.URL)
