from django.shortcuts import render, redirect
from .models import Category, Drink


def category_view(request):
    if request.method == 'GET':
        return render(request, 'choose.html')
    elif request.method == 'POST':
        cate = {'cold': '콜드 브루 커피', 'brewed': '브루드 커피', 'espre': '에스프레소'}
        if request.POST.get('cold'):
            category = Category.objects.get(category=cate['cold']).id
            drink = Drink.objects.filter(category_id=category)

        elif request.POST.get('brewed'):
            category = Category.objects.get(category=cate['brewed']).id
            drink = Drink.objects.filter(category_id=category)
        else:
            category = Category.objects.get(category=cate['espre']).id
            drink = Drink.objects.filter(category_id=category)

        return render(request, 'drink.html', {'drinks': drink})
