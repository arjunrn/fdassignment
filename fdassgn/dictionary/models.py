from django.db import models


class DictWord(models.Model):
    word = models.CharField(max_length=100, unique=True, blank=False)
    url = models.URLField(verbose_name='Full URL', name='URL', max_length=2000, db_index=True, null=True, default=None,
                          unique=True)
    ts = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Dictionary Word'
