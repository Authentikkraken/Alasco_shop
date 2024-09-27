from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.nom

class Produit(models.Model):
    titre = models.CharField(max_length=200)
    prix = models.FloatField()
    description = models.TextField()
    categorie = models.ForeignKey(Categorie,related_name='categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=600)
    date_ajout = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['-date_ajout']
    def __str__(self):
        return self.titre


class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=200,blank=False,null=False)
    prenom = models.CharField(max_length=200,blank=False, null=False)
    address = models.CharField(max_length=200,blank=False,null=False)
    numero = models.FloatField(blank=False, null=False)
    email = models.EmailField()
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return self.nom
