from django.contrib import admin
from django.contrib.admin import ModelAdmin
from dictionary.models import DictWord

admin.site.register(DictWord, ModelAdmin)
