from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class BLOG(models.Model):
    title = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='media/Blog')
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE,related_name='blog')
    Active = models.BooleanField(default=False)
    Featured = models.BooleanField(default=False)
    Description = models.TextField()
    def __str__(self):
        return self.title


class Contact(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone = models.IntegerField()
    addres = models.TextField()
    def __str__(self):
        return self.Name



