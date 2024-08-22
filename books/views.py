from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['published_date', 'title']

    def get_serializer_class(self):
        # Custom behavior: return a different serializer if needed
        return BookSerializer

    def perform_create(self, serializer):
        # Custom behavior: set an attribute on the book
        serializer.save()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
