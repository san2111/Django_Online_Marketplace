from django.shortcuts import render

from items.models import Category , Item


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categoryies = Category.objects.all()

    return render(request, 'app/index.html' ,{
        'categories' : categoryies,
        'items' : items,
    })

def contact(request):
    return render(request, 'app/contact.html')

