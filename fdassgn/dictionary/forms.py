from django import forms


class LongURL(forms.Form):
    url = forms.URLField(max_length=2000, min_length=5, label='URL')
