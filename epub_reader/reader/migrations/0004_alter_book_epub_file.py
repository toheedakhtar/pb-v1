# Generated by Django 4.1.7 on 2023-04-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0003_book_name_alter_book_epub_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='epub_file',
            field=models.FileField(null=True, upload_to='epub/'),
        ),
    ]
