# Generated by Django 4.1.7 on 2023-04-08 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0002_alter_book_epub_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='epub_file',
            field=models.FileField(null=True, upload_to='epubs/'),
        ),
    ]