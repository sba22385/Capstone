from rest_framework import serializers
from .models import Book
import re

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_isbn(self, value):
        if not re.match(r'^\d{10}(\d{3})?$', value):
            raise serializers.ValidationError("ISBN must be 10 or 13 digits.")
        return value