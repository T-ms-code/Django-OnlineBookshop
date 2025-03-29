from django.db import models
from django.urls import reverse


# Create your models here.
class Autor(models.Model):
    nume=models.CharField(max_length=50)
    prenume=models.CharField(max_length=50)
    data_nastere=models.DateField()
    data_deces=models.DateField(null=True,blank=True)
    nationalitate=models.CharField(max_length=50,null=True,blank=True)
    descriere=models.TextField(null=True,blank=True)
    premii=models.CharField(max_length=100,null=True,blank=True)
    
    def get_absolute_url(self):
        return reverse('detalii_autor', kwargs={'id': self.id})    




class Carte(models.Model):
    titlu=models.CharField(max_length=50)
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE, null=True, blank=True)
    nr_pagini=models.PositiveIntegerField()
    data_publicatie=models.DateField()
    coperta=models.ImageField(null=True, blank=True)
    pret=models.DecimalField(max_digits=10, decimal_places=2)
    stocuri=[('epuizat','Epuizat'),('neepuizat',"Neepuizat")]
    stoc=models.CharField(choices=stocuri, default='neepuizat')
    nr_stoc = models.PositiveIntegerField(default=20)
    librarii = models.ManyToManyField('Librarie', null=True, blank=True)
    edituri = models.ManyToManyField('Editura', null=True, blank=True)
    comenzi = models.ManyToManyField('Comanda', null=True, blank=True)
    categorii=[('liric','Liric'),('epic','Epic'),('dramatic','Dramatic'),('nonliteral','Nonliterar')]
    categorie = models.CharField(choices=categorii,default='epic',null=False, blank=False)
    
    def get_absolute_url(self):
        return reverse('detalii_carte', kwargs={'id': self.id})
    
    
class Recenzie(models.Model):
    nume_creator=models.CharField(max_length=50)
    prenume_creator=models.CharField(max_length=50)
    carte=models.ForeignKey(Carte,on_delete=models.CASCADE, null=True)
    data_creare=models.DateField(null=True)
    continut=models.TextField()
    actualizata=models.BooleanField()
    verificata=models.BooleanField()
    
    
class Librarie(models.Model):   
    denumire=models.CharField(max_length=50)
    data_infiintare=models.DateField(default='1990-01-01')
    email=models.EmailField(unique=True)
    telefon=models.CharField(max_length=20, null=True, unique=True)
    tara=models.CharField(max_length=50)
    oras=models.CharField(max_length=50)
    strada=models.CharField(max_length=50)
    carti = models.ManyToManyField(Carte, null=True, blank=True)


class Editura(models.Model):   
    denumire=models.CharField(max_length=50)
    data_infiintare=models.DateField(default='1990-01-01')
    email=models.EmailField(unique=True)
    tara=models.CharField(max_length=50)
    oras=models.CharField(max_length=50)
    strada=models.CharField(max_length=50)
    carti = models.ManyToManyField(Carte, related_name='ceva', null=True, blank=True)
    
    
class Comanda(models.Model):
    nr_produse=models.PositiveBigIntegerField()
    pret_total=models.DecimalField(max_digits=10, decimal_places=2)
    data_concepere=models.DateField(null=True)
    data_livrare=models.DateField(null=True)
    firma_livratoare=models.CharField(max_length=50)
    adresa_livrare=models.CharField(max_length=50)
    plati=[('card', 'Card'),('cash', 'Cash')]
    mod_plata=models.CharField(choices=plati, default='card')
    carti = models.ManyToManyField(Carte, null=True, blank=True)
    


    
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    telefon = models.CharField(max_length=15, blank=True)
    tara = models.CharField(blank=True)
    localitate=models.CharField(blank=True)
    strada = models.CharField(blank=True)
    gen = models.CharField(blank=True)
    cod = models.CharField(max_length=100, null=True, blank=True)
    email_confirmat = models.BooleanField(default=False)
    blocat = models.BooleanField(default=False)
    class Meta:
        permissions = [
            ("vizualizeaza_oferta", "Oferte doar pentru clientii privilegiati."),
        ]
        
    def get_absolute_url(self):
        return reverse('detalii_user', kwargs={'id': self.id})
    
    
    
class Vizualizari(models.Model):
    utilizator = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    produs = models.ForeignKey('Carte', on_delete=models.CASCADE)
    data_vizualizare = models.DateTimeField(auto_now_add=True)
    
    
    
class Promotii(models.Model):
    nume = models.CharField(null=False, blank=False)
    data_creare = models.DateTimeField(auto_now_add=True)
    data_expirare = models.DateTimeField(null=False, blank=False)
    subiect = models.CharField(null=True, blank=True)
    mesaj = models.TextField(null=True, blank=True)
    reducere = models.DecimalField(max_digits=3, decimal_places=1, null=False, blank=False)
    





