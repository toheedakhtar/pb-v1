from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .forms import BookForm
from .models import Book, ad_book
import os 
from django.conf import settings


import ebooklib
from ebooklib import epub
# from bs4 import BeautifulSoup
import html2text    


# Create your views here.

def home(request):
    return render(request, 'reader/index.html')



def reader(request, pk_count):

    my_model_instance = Book.objects.get(pk=pk_count)
    my_file = my_model_instance.epub_file.path
    book = epub.read_epub(my_file)

    content = ""


    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            html = item.get_content().decode('utf-8')
            text = html2text.html2text(html)
            content += text 

    filename = Book.filename(my_model_instance)

    context = {
        'content' : content,
        'filename': filename
    }
    return render(request, 'reader/reader.html', context)


def delete(request, book_id):
    Book.objects.get(pk=book_id).delete()

    return redirect('/books')

@login_required
def upload(request):
    
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        file = request.FILES['file']
        # file = request.POST.get('file', None)
        book = Book.objects.create(epub_file = file)
        book.save()
        return HttpResponseRedirect("/books")
    else:
        form = BookForm

    return render(request, 'reader/upload.html', {'form': form})
  
    
@login_required
def books(request):

    items = Book.objects.all()
    return render(request, 'reader/books.html', {'items': items})

def admin_books(request):
    items = ad_book.objects.all()
    return render(request, 'reader/admin_books.html', {'items': items})

def ad_reader(request, pk_count):

    my_model_instance = ad_book.objects.get(pk=pk_count)
    my_file = my_model_instance.epub_file_ad.path
    book = epub.read_epub(my_file)

    content = ""


    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            html = item.get_content().decode('utf-8')
            text = html2text.html2text(html)
            content += text 

    filename = ad_book.filename(my_model_instance)

    context = {
        'content' : content,
        'filename': filename
    }
    return render(request, 'reader/reader.html', context)



def feedback(request):
    if request.method == "POST":
        name = request.POST["message_name"]
        email = request.POST['message_email']
        message = request.POST["message"]

        send_mail(
            name,
            message,
            email,
            ['pixbook001@gmail.com'],)

        return render(request , 'reader/feedback.html', {'message_name': name})

    else:
        return render(request , 'reader/feedback.html')