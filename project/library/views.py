from django.shortcuts import render, get_object_or_404
from .models import Category, Book

def home(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    return render(request, "home.html", {'categories': categories, 'books': books})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def book_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    books = Book.objects.filter(category=category)
    return render(request, 'books_by_category.html', {'category': category, 'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def books_list(request):
    books = Book.objects.all()  # Barcha kitoblarni olish
    return render(request, 'books_list.html', {'books': books})
