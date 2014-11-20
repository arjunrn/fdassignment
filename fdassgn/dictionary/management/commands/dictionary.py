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
        if len(args) != 1:
            raise CommandError('Input file not specified.')
        if not os.path.exists(args[0]):
            raise CommandError('The specified file does not exist.')
        cleaned_words = []
        with open(args[0], 'r') as words:
            for word in words:
                cleaned_words.append(self.clean_word(word))
        unique_words = list(set(cleaned_words))

        duplicates = DictWord.objects.all()
        for d in duplicates:
            if d.word in unique_words:
                unique_words.remove(d.word)

        if unique_words:
            unique_words.sort(reverse=True)
            DictWord.objects.bulk_create([DictWord(word=w) for w in unique_words])
            print('%d new words were added:' % len(unique_words))
        else:
            print('No new words were added')
