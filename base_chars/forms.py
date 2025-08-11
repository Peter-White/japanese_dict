from django import forms
from base_chars import models

class GanaForm(forms.Form):
    symbol = forms.CharField(max_length=2, help_text=u'Enter the native hiragana symbol')
    romaji = forms.CharField(max_length=3, help_text=u'Enter the romaji translation')

class KanaForm(forms.Form):
    symbol = forms.CharField(max_length=2, help_text=u'Enter the native katakana symbol')
    romaji = forms.CharField(max_length=3, help_text=u'Enter the romaji translation')