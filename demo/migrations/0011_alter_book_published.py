# Generated by Django 3.2.20 on 2023-08-29 16:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0010_book_cover_book_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
