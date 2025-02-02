# test_models.py
from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def test_translation_fallback(self):
        faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
        translated_question = faq.get_translated_text("question", "hi")
        print(translated_question)
        self.assertIsNotNone(translated_question)