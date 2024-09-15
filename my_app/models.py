from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Lace(models.Model):
  color = models.CharField(max_length=20)
  
  def __str__(self):
    return self.color
  
  def get_absolute_url(self):
    return reverse('lace_detail', kwargs={'pk': self.id})
  
class Shoe(models.Model):
  model = models.CharField(max_length=50)
  brand = models.CharField(max_length=20)
  purchase_date = models.DateField()
  size = models.DecimalField(max_digits=4, decimal_places=1)
  price = models.DecimalField(max_digits = 10, decimal_places = 2)
  description = models.TextField(max_length=250)
  current_condition=models.CharField(
    choices=[('1', 'Deadstock'), ('2', 'VNDS'), ('3', 'NDS'), ('4', 'Used'), ('5', 'Very Used')]
  )
  photo = models.ImageField(upload_to='shoes/', blank = True)
  laces = models.ManyToManyField(Lace)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.model
  
  def get_absolute_url(self):
    return reverse("shoe_detail", kwargs={"shoe_id": self.id})
