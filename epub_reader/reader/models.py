import os
from django.db import models

class Book(models.Model):
    epub_file = models.FileField(upload_to='epub/',null=True)

    def __str__(self):
            return self.epub_file.name

    def filename(self):
        return os.path.basename(self.epub_file.name)
    
class ad_book(models.Model):
    epub_file_ad = models.FileField(upload_to='ad_epub/',null=True)

    def __str__(self):
            return self.epub_file_ad.name

    def filename(self):
        return os.path.basename(self.epub_file_ad.name)