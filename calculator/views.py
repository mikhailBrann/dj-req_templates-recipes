from django.shortcuts import render,reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    template_path = 'home.html'
    pages = {
        'Омлет': '/omlet/',
        'Паста': '/pasta/',
        'Бутер (бутерброд)': '/buter/'
    }

    context = {
        "pages": pages
    }

    return render(request, template_path, context)

# Напишите ваш обработчик. Используйте DATA как источник данных
def calculator(request, recipe_name):
    # Результат - render(request, 'calculator/home.html', context)
    template_path = 'calculator/index.html'

    # проверяем, указал ли пользователь ключ
    servings = int(request.GET.get('servings', 1))

    # очищаем занвание блюда от лишних символов и проверяем есть ли оно в словаре
    recipe_name = recipe_name.replace("/", "")
    recipe = DATA[recipe_name].copy() if recipe_name in DATA else {}

    if recipe and servings > 1:
        for key, value in recipe.items():
            recipe[key] = value * servings

    # В качестве контекста должен быть передан словарь с рецептом:
    context = {
        "recipe": recipe
    }

    return render(request, template_path, context)