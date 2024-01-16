from django.db import models

class Birim(models.Model):
    birim_ad = models.CharField(max_length=255)
    ust_birim = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, null=True,)  

class Kullanici(models.Model):
    kullanici_ad = models.CharField(max_length=255)
    email = models.EmailField()
    sifre = models.CharField(max_length=255)
    birim = models.ForeignKey(Birim, on_delete=models.CASCADE)
    ilce = models.CharField(max_length=255)
    mahalle = models.CharField(max_length=255)
    user_type = models.CharField(max_length=50) 

class Personel(models.Model):
    personel_ad = models.CharField(max_length=255)
    pozisyon = models.CharField(max_length=255)
    birim = models.ForeignKey(Birim, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50) 