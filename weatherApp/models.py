from django.db import models

# Create your models here.

class SearchCity(models.Model):
    city=models.CharField(max_length=50, verbose_name='Город')
    temperature= models.IntegerField(verbose_name='Температура')
    sent_at=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    updated= models.DateTimeField(auto_now=True, verbose_name='обновленное время')


    def __str__(self):
       return self.city