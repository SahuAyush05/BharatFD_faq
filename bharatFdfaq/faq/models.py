from django.db import models
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
import googletrans
from googletrans import Translator
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class FAQ(models.Model):
    translator = Translator()
    LANGUAGES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ]
    
    question = models.TextField(verbose_name=_('Question'))
    answer = RichTextField(verbose_name=_('Answer'))
    question_hi = models.TextField(blank=True, null=True, verbose_name=_('Question (Hindi)'))
    question_bn = models.TextField(blank=True, null=True, verbose_name=_('Question (Bengali)'))
    answer_hi = RichTextField(blank=True, null=True, verbose_name=_('Answer (Hindi)'))
    answer_bn = RichTextField(blank=True, null=True, verbose_name=_('Answer (Bengali)'))

    def save(self, *args, **kwargs):
        # Auto-translate the question and answer if fields are empty
        for lang in ['hi', 'bn']:
            if not getattr(self, f'question_{lang}'):
                setattr(self, f'question_{lang}', self.translate_text(self.question, lang))
            if not getattr(self, f'answer_{lang}'):
                setattr(self, f'answer_{lang}', self.translate_text(self.answer, lang))
        
        super().save(*args, **kwargs)

    def translate_text(self, text, dest_lang):
        """Translates text using Google Translate API."""
        if not text:
            return ''
        cache_key = f'translation_{text}_{dest_lang}'
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation
        try:
            translation = self.translator.translate(text, dest=dest_lang).text
            cache.set(cache_key, translation, timeout=86400)  # Cache for a day
            return translation
        except Exception:
            return text  # Fallback to original text if translation fails
    
    def get_translated_text(self, field, lang='en'):
        """Returns the translated text based on the selected language."""
        translated_field = f'{field}_{lang}'
        return getattr(self, translated_field, getattr(self, field))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')



            