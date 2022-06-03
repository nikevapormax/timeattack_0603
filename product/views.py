from django.shortcuts import render, redirect
from .models import Category, Drink


def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'choose.html', {'categories': categories})
    elif request.method == 'POST':
        cate = {'cold': '콜드 브루 커피', 'brewed': '브루드 커피', 'espre': '에스프레소'}
        if request.POST.get('cold'):
            print('여기1')
            category = Category.objects.get(category=cate['cold']).id
            drink = Drink.objects.filter(category_id=category)
            print(drink)
            drinks = {}
            for i, d in enumerate(drink):
                drinks[i] = d.drink
            print(drinks)
        elif request.POST.get('brewed'):
            print('여기2')
            category = Category.objects.get(category=cate['brewed']).id
            drink = Drink.objects.filter(category_id=category)
            drinks = {}
            for i, d in enumerate(drink):
                drinks[i] = d.drink
            print(drinks)
        else:
            print('여기3')
            category = Category.objects.get(category=cate['espre']).id
            drink = Drink.objects.filter(category_id=category)
            drinks = {}
            for i, d in enumerate(drink):
                drinks[i] = d.drink
            print(drinks)
        return render(request, 'drink.html', drinks)
