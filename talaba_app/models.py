from django.db import models

# Create your models here.

jins = [
    ("Ayol", "Ayol"),
    ("Erkak", "Erkak")
    
]

class Talaba(models.Model):
    ism = models.CharField(max_length=300)
    familiya = models.CharField(max_length=300)
    tug_yil = models.DateTimeField(auto_now_add=False)
    tel = models.IntegerField()
    jins = models.CharField(max_length=200, choices=jins)
    
    def __str__(self):
        return self.ism
    
