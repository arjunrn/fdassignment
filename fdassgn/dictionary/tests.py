from django.core.urlresolvers import reverse
from django.test import TestCase
from dictionary.models import DictWord


class TestLink(TestCase):
    def setUp(self):
        DictWord.objects.create(word='something')
        DictWord.objects.create(word='this')
        DictWord.objects.create(word='that')

    def test_link(self):
        for url in ['http://something.com', 'http://example.com/this', 'http://example.com/that']:
            response = self.client.post(reverse('home'), data={'url': url})
            self.assertEqual(response.status_code, 302)

        self.assertEqual(DictWord.objects.get(word='something').URL, 'http://something.com')
        self.assertEqual(DictWord.objects.get(word='this').URL, 'http://example.com/this')
        self.assertEqual(DictWord.objects.get(word='that').URL, 'http://example.com/that')

    def test_exhaustion(self):
        for url in ['http://something.com', 'http://example.com/this', 'http://example.com/that', 'http://google.com']:
            self.client.post(reverse('home'), data={'url': url})
        self.assertEqual(DictWord.objects.get(word='something').URL, 'http://google.com')