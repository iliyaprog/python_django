from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from logic_library.models import BookModel, AuthorModel


def main_page_view(request):
    all_books = BookModel.objects.all()
    paginator = Paginator(all_books, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main_page.html', {'page_obj': page_obj})


class DetailBook(View):

    def get(self, request, book_id):
        book = BookModel.objects.get(id=book_id)
        return render(request, 'detail_book.html', {'book': book})


class DetailAuthor(View):

    def get(self, request, author_id):
        author = AuthorModel.objects.get(id=author_id)
        all_books = BookModel.objects.filter(author=author)
        return render(request, 'detail_author.html', {'author': author, 'all_books': all_books})
