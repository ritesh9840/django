from django.contrib import admin

# Register your models here.
from .models import Book
#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title','description','price']
    list_display = ['title','description','price']
    list_filter = ['published','price']
    search_fields = ['title','price']


