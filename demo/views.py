from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets

from .models import Book
from django.shortcuts import render
from .serializers import  BookSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Another(View):

    #books= Book.objects.all()  #this will retrive all book from database
    books = Book.objects.get(id=7) #return one record
    books = Book.objects.filter(is_published=True)
    output=''
    for book in books:
        output += f"We have {book.title}  books  with id {book.id}  in our database <br>"

   # output=f" We have {len(books) }  books in our database"


    def get(self,request):
        #return HttpResponse ('This is another function inside classs')
        return HttpResponse(self.output)

def first(request):

    return HttpResponse ('First message from response')

def second(request):

    books=Book.objects.all()
    #return render (request,'first_template.html',{'data':'this is data from view'})
    return render(request, 'first_template.html', {'books': books})

class BookViewSet(viewsets.ModelViewSet):
    serializer_class= BookSerializers
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)