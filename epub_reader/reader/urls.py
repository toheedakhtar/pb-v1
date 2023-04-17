from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.upload, name='upload'),
    path('reader/<int:pk_count>', views.reader, name='reader'),
    path('delete/<int:book_id>', views.delete, name='delete'),
    path('books/', views.books, name='books'),
    path('ad_books/', views.admin_books, name='ad_books'),
    path('ad_reader/<int:pk_count>', views.ad_reader, name='ad_reader'),
    path('feedback/', views.feedback, name='feedback'),
    

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
