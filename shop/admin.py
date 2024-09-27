from django.contrib import admin

# Register your models here.
from .models import Categorie, Produit, Commande

admin.site.site_header = 'E-commerce'
admin.site.site_title = 'Alsco Shop'
admin.site.index_title = 'Alsco Shop'


class AdminCategorie(admin.ModelAdmin):
    list_display = ('nom', 'date_added')

class AdminProduit(admin.ModelAdmin):
    list_display = ('titre', 'prix','categorie', 'date_ajout')
    search_fields = ['titre']
    list_editable = ['prix']

class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'prenom', 'numero', 'address', 'ville', 'email', 'pays','total', 'date_commande')

admin.site.register(Produit,AdminProduit)
admin.site.register(Categorie, AdminCategorie)
admin.site.register(Commande, AdminCommande)


