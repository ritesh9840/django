# Generated by Django 4.2.4 on 2023-08-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(choices=[('J', 'Java'), ('P', 'Python')], max_length=36, unique=True),
        ),
    ]