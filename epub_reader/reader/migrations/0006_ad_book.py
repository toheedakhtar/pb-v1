# Generated by Django 4.1.7 on 2023-04-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0005_remove_book_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ad_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
