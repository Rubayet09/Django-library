from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('non-optimized/', views.BookListViewNonOptimized.as_view(), name='book-list-non-optimized'),
    path('optimized/', views.BookListViewOptimized.as_view(), name='book-list-optimized'),
    path('prefetch-related/', views.BookListViewPrefetchRelated.as_view(), name='book-list-prefetch-related'),
]