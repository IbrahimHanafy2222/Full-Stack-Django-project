from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField()
    discount = models.PositiveIntegerField(default=0)  # Save percentage (e.g., 60)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # e.g. 498.00
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # e.g. 1245.00
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name 

class Best_Selling(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name 
    
class New_Arrival(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField()
    old= models.DecimalField(max_digits=10, decimal_places=2)
    new= models.DecimalField(max_digits=10, decimal_places=2)
    discount= models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name 

class Pants(models.Model):
    name= models.CharField(max_length=255)

    image = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

class Winter(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField()
    old= models.DecimalField(max_digits=10, decimal_places=2)
    new= models.DecimalField(max_digits=10, decimal_places=2)
    discount= models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name 
    
class Men(models.Model):
  
    name = models.CharField(max_length=255)
    image = models.TextField()
    old= models.DecimalField(max_digits=10, decimal_places=2)
    new= models.DecimalField(max_digits=10, decimal_places=2)
    discount= models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name 