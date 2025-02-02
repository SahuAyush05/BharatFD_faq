from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        request = self.context.get('request', None)
        lang = request.GET.get('lang', 'en') if request else 'en'
        if lang not in ['hi', 'bn']:
            lang = 'en'

        data = {
            "id": instance.id,
            "question": getattr(instance, f'question_{lang}', instance.question),
            "answer": getattr(instance, f'answer_{lang}', instance.answer)
        }
        
        return data

    class Meta:
        model = FAQ
        fields = ["id", "question", "answer"]
