from django.urls import path
from . import views


from django.contrib.sitemaps.views import sitemap
from .sitemaps import AutorSitemap, CarteSitemap, CustomUserSitemap, VederiStaticeSitemap

sitemaps = {
    'autor': AutorSitemap,
    'carte': CarteSitemap,
    'user': CustomUserSitemap,
    'static': VederiStaticeSitemap,
}



urlpatterns = [
	path("", views.index, name="index"),
    path("carte_filtrare_titlu/", views.carte_filtrare_titlu, name="1"),
    path("carte_filtrare_autor/", views.carte_filtrare_autor, name="2"),
    path("carte_filtrare_nr_pagini/", views.carte_filtrare_nr_pagini, name="3"),
    path("carte_filtrare_pret/", views.carte_filtrare_pret, name="4"),
    path("paginare/", views.paginare, name="5"),
    path("cartifilterform/", views.carti_filter_form, name="6"),
    path("contact/", views.captare_contact, name="7"),
    path("adauga_autor/", views.adauga_autor, name="8"),
    path("home", views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout2, name="logout2"),
    path("inregistrare", views.register_view, name="11"),
    path('schimba_parola/', views.schimba_parola, name='schimba_parola'),
    path('confirma_email/<str:cod>/', views.confirma_email, name='confirma_email'),
    path('adauga_vizualizare/', views.adauga_vizualizare,name='adauga_vizualizare'),
    path('promotii/', views.adauga_promotie,name='adauga_promotie'),
    path('pagina_acces_oferte/', views.pagina_acces_oferte,name='pagina_acces_oferte'),
    path('da_permisiune/', views.da_permisiune,name='da_permisiune'),
    path('oferta/', views.oferta, name='oferta'),
    path('detalii_carte/<int:id>', views.detalii_carte, name='detalii_carte'),
    path('detalii_autor/<int:id>', views.detalii_autor, name='detalii_autor'),
    path('detalii_user/<int:id>', views.detalii_user, name='detalii_user'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('cos_virtual/', views.cos_virtual, name='cos_virtual'),
    path('cumpara_cos/', views.cumpara_cos, name='cumpara_cos'),
    path('meniu/', views.meniu, name='meniu'),
]
