from django.shortcuts import render
from .models import *

def home(request):
    category = request.GET.get("category")
    if category == None:
        card_values = CardValues.objects.all()
    else:
        card_values = CardValues.objects.filter(category__category_name=category)
    context = {
        "card_values": card_values,
        "category":Category.objects.all(),
    }
    return render(request, 'pages/home.html', context)
