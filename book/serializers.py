from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'photo', 'full_name', 'bio')


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'full_name', 'photo')


class BookSerializer(serializers.ModelSerializer):
    author = BookAuthorSerializer()

    class Meta:
        model = Book
        fields = ('id', 'image', 'name', 'description', 'author')