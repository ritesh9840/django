# Generated by Django 4.2.4 on 2023-08-24 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_alter_book_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateTimeField(auto_now=True),
        ),
    ]