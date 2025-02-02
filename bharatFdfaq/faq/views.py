from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from django.utils.translation import activate
from googletrans import Translator
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    
    @action(detail=True, methods=['get'])
    def translated(self, request, pk=None):
        faq = self.get_object()
        lang = request.GET.get('lang', 'en')
        translated_data = {
            'id': faq.id,
            'question': faq.get_translated_text('question', lang),
            'answer': faq.get_translated_text('answer', lang)
        }
        return Response(translated_data)