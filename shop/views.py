from django.shortcuts import render, redirect
from .models import Produit, Commande
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_object = Produit.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
       product_object = Produit.objects.filter(titre__icontains = item_name)

    paginator = Paginator(product_object, 25)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_object':product_object})

def detail(request, myid):
    product_object = Produit.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product':product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        numero = request.POST.get('numero')
        address = request.POST.get('address')
        email = request.POST.get('email')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        com = Commande(items = items,total = total, nom=nom, prenom=prenom,numero= numero, address = address, email = email, ville = ville , pays = pays , zipcode = zipcode)
        com.save()
        return redirect('confirmation')
    return render(request, 'shop/checkout.html')

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'shop/confirmation.html', {'nom':nom})