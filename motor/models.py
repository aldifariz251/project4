from django.db import models

# Create your models here.
class Motor(models.Model):
    nama = models.CharField(max_length=100, null= True)
    merk = models.CharField(max_length=100, null= True)
    plat = models.CharField(max_length=100, null= True)
    telp = models.CharField(max_length=100, null= True)
    email = models.CharField(max_length=100, null= True)

    class Meta():
        __tablename__ = "Motor"

    def __str__(self):
        return(self).nama

    