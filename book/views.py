from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Book, Author
from .serializers import *
from rest_framework.generics import ListAPIView
from .serializers import AuthorSerializer



class BookAPIView(APIView):
    def get(self, request, pk=None):
        # Agar pk bo'lsa → bitta kitob, bo'lmasa → barcha kitoblar
        if pk:
            book = get_object_or_404(Book.objects.select_related('author'), pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            books = Book.objects.select_related('author').all()
            serializer = BookSerializer(books, many=True, context={"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()