from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book_md

# Create your views here.


def book_list(request):
    books = Book_md.objects.all()
    return render(request, 'book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        publisher = request.POST['publisher']
        publication_date = request.POST['publication_date']
        isbn = request.POST['isbn']
        category = request.POST['category']
        if Book_md.objects.filter(isbn=isbn).exists():
            messages.error(request, f"Book with ISBN number:{isbn} already exists")
            return HttpResponseRedirect('/new')

        book = Book_md(title=title, author=author, publisher=publisher,
                       publication_date=publication_date, isbn=isbn, category=category)
        book.save()
        messages.success(request, f'Book "{title}" has been added!')
        return HttpResponseRedirect('/')
    else:
        return render(request, 'add_book.html')


def update_book(request, id):
    book = get_object_or_404(Book_md, book_id=id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publisher = request.POST.get("publisher")
        book.publication_date = request.POST.get("publication_date")
        book.isbn = request.POST.get("isbn")
        book.category = request.POST.get("category")
        if Book_md.objects.filter(isbn=request.POST.get('isbn')).exists():
            messages.error(
                request, f"Book with ISBN number:{request.POST.get('isbn')} already exists")
            return HttpResponseRedirect('/new')
        book.save()
        messages.success(
            request, f'Book "{request.POST.get("title")}" has been Updated!')
        return redirect("book_list")
    else:
        context = {"book": book}
        return render(request, "update_book.html", context)


def delete_book(request, id):
    book = get_object_or_404(Book_md, book_id=id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, f'Book "{book.title}" has been deleted!')
        return redirect('book_list')
    else:
        context = {'book': book}
        return render(request, 'delete_book.html', context)


def search_books(request):
    if request.method == 'POST':
        query = request.POST['query']
        return redirect(reverse('search_results', kwargs={'query': query, 'page': 1}))
    else:
        return render(request, 'search.html')


def search_results(request, query, page):

    results = Book_md.objects.filter(
        Q(title__icontains=query) | Q(
            author__icontains=query) | Q(category__icontains=query)
    )
    length = len(results)
    paginator = Paginator(results, 10)
    page_obj = paginator.get_page(page)
    return render(request, 'search_results.html', {'length': length, 'books': page_obj, 'query': query})
