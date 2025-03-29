from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Autor, Carte, CustomUser


class AutorSitemap(Sitemap):
    changefreq = 'daily'  
    priority = 0.9        

    def items(self):
        return Autor.objects.all()
    

class CarteSitemap(Sitemap):
    changefreq = "monthly"  
    priority = 0.8        

    def items(self):
        return Carte.objects.all()


class CustomUserSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return CustomUser.objects.filter(is_active=True)
    
    
    
class VederiStaticeSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        # Numele view-urilor/URLS statice
        return ['index', '5', '7']

    def location(self, item):
        # Returneaza URL-ul pentru fiecare item
        # Atentie, acestea trebuie sa aiba name specificat in urls.py
        return reverse(item)
