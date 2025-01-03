from django.views.generic import ListView
from django.db.models import Prefetch
from .models import Book


class BookListViewNonOptimized(ListView):
    model = Book
    template_name = 'library/book_list_non_optimized.html'
    context_object_name = 'books'
    paginate_by = 1000

    def get_queryset(self):
        """
        Non-optimized query - will cause N+1 problem
        """
        return Book.objects.all()

class BookListViewOptimized(ListView):
    model = Book
    template_name = 'library/book_list_optimized.html'
    context_object_name = 'books'
    paginate_by = 1000

    def get_queryset(self):
        """
        Optimized query using select_related
        """
        return Book.objects.select_related('author', 'publisher').all()
    
class BookListViewPrefetchRelated(ListView):
    model = Book
    template_name = 'library/book_list_prefetch_related.html'
    context_object_name = 'books'
    paginate_by = 1000

    def get_queryset(self):
        return Book.objects.prefetch_related('author', 'publisher').all()