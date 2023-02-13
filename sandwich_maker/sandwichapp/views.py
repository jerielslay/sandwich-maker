from django.shortcuts import render
from django.http import Http404
from django.views import View
import random

# Create your views here.
ingredients = {
    'meats': ['honey glazed turkey', 'beef salami', 'chicken cutlet', 'pastrami', 'ham'],
    'cheeses': ['mozzarella', 'provolone', 'muenster', 'american', 'pepper jack'],
    "toppings": ['onions', 'sweet peppers', 'lettuce', 'tomato', 'avocado' ],
}

class SandwichappView(View):
    def get(self, request):
        return render(
            request = request,
            template_name = 'sandwichapp.html',
            context = {'ingredients': ingredients.keys()}
        )

class IngredientsView(View):
    def get(self, request, ingredient_type):
        if ingredient_type not in ingredients:
            raise Http404(f"WHOA WHOA!, There's No Such Ingredient!: {ingredient_type}")

        return render (
            request = request,
            template_name = "ingredients_list.html",
            context = {
                'ingredients': ingredients[ingredient_type],
                'ingredient_type': ingredient_type,
            }
        )

class SandwichGeneratorView(View):
    def get(self, request):
            selected_meat = random.choice(ingredients['meats'])
            selected_cheese = random.choice(ingredients['cheeses'])
            selected_toppings = random.choice(ingredients['toppings'])

            sandwich = f'{selected_meat} & {selected_cheese} with {selected_toppings}'
            return render(request, 'sandwich_generator.html', context = { 'sandwich' : sandwich})

class MenuView(View):
    def get(self,request):
        menus=[]
        for meat in ingredients['meats']:
            for cheese in ingredients['cheeses']:
                for topping in ingredients ['toppings']:
                    sandwich = f'{meat} & {cheese} with {topping}'
                    menus.append(sandwich)

        return render(request, 'menu.html', context = { 'menus' : menus})