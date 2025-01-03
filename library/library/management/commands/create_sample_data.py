# from django.core.management.base import BaseCommand
# from library.models import Author, Publisher, Book
# from datetime import date

# class Command(BaseCommand):

#     def handle(self, *args, **kwargs):
#         # Create author
#         author = Author.objects.create(
#             name='Humayun Ahmed',
#             email='humayun@gmail.com',
#             bio='A great Bangladeshi author'
#         )
#         self.stdout.write(self.style.SUCCESS('Created author'))

#         # Create publisher
#         publisher = Publisher.objects.create(
#             name='Anondo Publisher',
#             address='Bangla Motor',
#             website='http://anondo-publication-ltd.com'
#         )
#         self.stdout.write(self.style.SUCCESS('Created publisher'))

#         # Create books
#         for i in range(10):
#             Book.objects.create(
#                 book_id=f'BOOK{i+1}',
#                 title=f'Book Title {i+1}',
#                 author=author,
#                 publisher=publisher,
#                 publication_date=date.today(),
#                 isbn=f'123333{i}',
#                 available=True
#             )
        
#         self.stdout.write(self.style.SUCCESS('Created 10 books'))


from django.core.management.base import BaseCommand
from library.models import Author, Publisher, Book
from datetime import date
from random import randint, choice


class Command(BaseCommand):
    help = 'Creates sample data for illustrating select_related and prefetch_related'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Book.objects.all().delete()
        Author.objects.all().delete()
        Publisher.objects.all().delete()

        self.stdout.write(self.style.WARNING('Cleared existing data'))

        # Create publishers
        publishers = []
        for i in range(5):
            publisher = Publisher.objects.create(
                name=f'Publisher {i+1}',
                address=f'Address {i+1}',
                website=f'http://publisher{i+1}.com'
            )
            publishers.append(publisher)
        self.stdout.write(self.style.SUCCESS('Created 5 publishers'))

        # Create authors
        authors = []
        for i in range(10):
            author = Author.objects.create(
                name=f'Author {i+1}',
                email=f'author{i+1}@example.com',
                bio=f'Bio for author {i+1}'
            )
            authors.append(author)
        self.stdout.write(self.style.SUCCESS('Created 10 authors'))

        # Create books
        for i in range(50):
            book = Book.objects.create(
                book_id=f'BOOK{i+1}',
                title=f'Book Title {i+1}',
                author=choice(authors),
                publisher=choice(publishers),
                publication_date=date.today(),
                isbn=f'123456789012{i}',
                available=bool(randint(0, 1))
            )
        self.stdout.write(self.style.SUCCESS('Created 50 books'))