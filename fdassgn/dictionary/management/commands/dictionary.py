from django.core.management import BaseCommand, CommandError
import os
import re
from dictionary.models import DictWord


class Command(BaseCommand):
    help = 'Creates the Word List'
    args = '<file_with_words>'
    cleaner = re.compile(r'[^a-z0-9]')

    def clean_word(self, word):
        return self.cleaner.sub('', word.lower())

    def handle(self, *args, **options):
        if not os.path.exists(args[0]):
            CommandError('The specified file does not exist.')
        cleaned_words = []
        with open(args[0], 'r') as words:
            for word in words:
                cleaned_words.append(self.clean_word(word))
        unique_words = list(set(cleaned_words))
        DictWord.objects.bulk_create([DictWord(word=w) for w in unique_words])
