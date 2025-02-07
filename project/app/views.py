from django.shortcuts import render , redirect

from items.models import Category , Item

from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categoryies = Category.objects.all()

    return render(request, 'app/index.html' ,{
        'categories' : categoryies,
        'items' : items,
    })

def contact(request):
    return render(request, 'app/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:

      form = SignupForm()

    return render(request, 'app/signup.html',{
        'form':form
    })  
