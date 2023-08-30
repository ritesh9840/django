from django.db import models
from django.utils import timezone


# Create your models here.
class BookNumber(models.Model):
    isbn_10=models.CharField(max_length=10,blank=True)
    isbn_13=models.CharField(max_length=13,blank=True)



class Book(models.Model ):
    # TITLES= (
    #     ('J', 'Java'),
    #     ('P','Python')
    # )
    title=models.CharField(blank=False,unique=True,max_length=36)#choices=TITLES)
    description=models.TextField(max_length=256,default='n/a')
    price=models.DecimalField(default=0,decimal_places=2,max_digits=12)
    published=models.DateTimeField(default=timezone.now)
    is_published=models.BooleanField(default=False)
    cover=models.ImageField(upload_to='covers/',blank=True)
    number=models.OneToOneField(BookNumber,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
