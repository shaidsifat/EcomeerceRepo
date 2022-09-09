from django.db import models

# Create your models here.



class product(models.Model):

    name = models.CharField(max_length=50)
    stock = models.IntegerField(max_length=20)
    price = models.IntegerField(max_length=20)
    image1 = models.ImageField(upload_to='media/post_image',blank=True)
    image2 = models.ImageField(upload_to='media/post_image',blank=True)

    def __str__(self):
      return self.name


class Order(models.Model):

    product = models.ForeignKey(product,on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(max_length=10,null=True,blank=True)
    delivery = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return str(self.id)