from django.contrib import admin

# Register your models here.
from .models import Carte
# admin.site.register(Carte)

from .models import Autor
# admin.site.register(Autor)

from .models import Recenzie
# admin.site.register(Recenzie)

from .models import Librarie
# admin.site.register(Librarie)

from .models import Editura
# admin.site.register(Editura)


from .models import Comanda
# admin.site.register(Comanda)



class AutorAdmin(admin.ModelAdmin):
    list_display = ('nume', 'prenume','descriere', 'nationalitate','data_nastere', 'data_deces', 'premii')  
    list_filter=('nume','prenume')
    search_fields=('nume',)
admin.site.register(Autor, AutorAdmin)

class CarteAdmin(admin.ModelAdmin):
    list_display=('titlu',)
    list_filter=('titlu','autor')
    search_fields=('titlu',)
admin.site.register(Carte, CarteAdmin)


class RecenzieAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Informații principale', {
            'fields': ('continut','carte')
        }),
        ('Informații secundare', {
            'fields': ('nume_creator','prenume_creator', 'data_creare', 'actualizata', 'verificata'),
            'classes': ('collapse',),  # secțiune pliabilă
        }),)
    list_filter=('nume_creator','prenume_creator')
    search_fields=('nume_creator',)
admin.site.register(Recenzie, RecenzieAdmin)

class LibrarieAdmin(admin.ModelAdmin):
    list_filter=('denumire','oras')
    search_fields=('denumire',)
admin.site.register(Librarie, LibrarieAdmin)

class EdituraAdmin(admin.ModelAdmin):
    list_filter=('denumire','oras')
    search_fields=('denumire',)
admin.site.register(Editura, EdituraAdmin)

class ComandaAdmin(admin.ModelAdmin):
    list_filter=('nr_produse','mod_plata')
    search_fields=('nr_produse',)
admin.site.register(Comanda, ComandaAdmin)



admin.site.site_header = "Magazinul  X de carti online"
admin.site.site_title = "Patronul magazinului"
admin.site.index_title = "Bine ai venit în panoul de administrare, Mihai!"



from .models import CustomUser
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'password', 'email')     
# admin.site.register(CustomUser, CustomUserAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'blocat')  
    list_filter = ('is_staff', 'is_superuser', 'blocat')  
    search_fields = ('username', 'email')  

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []  # Superuserii pot vedea toate campurile
        if request.user.groups.filter(name="Moderatori").exists():
            # Moderatorii pot vedea doar aceste campuri
            return [field.name for field in self.model._meta.fields if field.name not in ('first_name', 'last_name', 'email', 'blocat')]
        #Alti utilizatori (DIN STUFF) nu pot vedea nimic
        return [field.name for field in self.model._meta.fields]

    #NU E NEVOIE DE EA, CACI ORICUM moderatorii AU PERMISIUNEA CHANGE!
    # def has_change_permission(self, request, obj=None):
    #     # Permite doar modificarea utilizatorilor doar pentru c=superuseri si moderatori
    #     if request.user.is_superuser:
    #         return True
    #     return request.user.groups.filter(name="Moderatori").exists()
admin.site.register(CustomUser, CustomUserAdmin)



from .models import Vizualizari
class VizualizariAdmin(admin.ModelAdmin):
    list_display = ('utilizator', 'produs')     
admin.site.register(Vizualizari, VizualizariAdmin)