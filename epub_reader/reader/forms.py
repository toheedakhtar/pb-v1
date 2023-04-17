from django import forms
from reader.models import Book

# class upload_file(forms.Form):
#     # title = forms.CharField(max_length=64)/
#     file = forms.FileField()


class BookForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = Book
        fields = ['file']
