from datetime import datetime
from django.db import models, transaction



class DictWord(models.Model):
    word = models.CharField(max_length=100, unique=True, blank=False)
    url = models.URLField(verbose_name='Full URL', name='URL', max_length=2000, db_index=True, null=True, default=None,
                          unique=True)
    ts = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return self.word

    def set_url(self, url):
        with transaction.atomic():
            self.ts = datetime.now()
            self.URL = url
            self.save()

    class Meta:
        verbose_name = 'Dictionary Word'
