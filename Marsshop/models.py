from django.db import models
from app.models import User
# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='shop/')
    cost = models.IntegerField()
    quantitiy = models.IntegerField()



    def __str__ (self) -> str:
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return super().__str__()
    

class Hackaton (models.Model):
    text = models.TextField()
    