#from django.shortcuts import render*/

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Book

def home(request):
    return render(request, 'home.html')

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_details.html', {'book': book})
