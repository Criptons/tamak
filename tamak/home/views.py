from django.shortcuts import render

meal = [
    {
        "food_name" : "Плов",
        "food_price": 190,
        "food_time_to_deliver": "150 минут",
        "portion": "600 грамм"
    },
    {
        "food_name" : "Лагман",
        "food_price": 170,
        "food_time_to_deliver": "120 минут",
        "portion": "600 грамм"
    },
    {
        "food_name" : "Манты",
        "food_price": 210,
        "food_time_to_deliver": "90 минут",
        "portion": "500 грамм"
    },{
        "food_name" : "Плов",
        "food_price": 190,
        "food_time_to_deliver": "150 минут",
        "portion": "600 грамм"
    },
    {
        "food_name" : "Лагман",
        "food_price": 170,
        "food_time_to_deliver": "120 минут",
        "portion": "600 грамм"
    },
    {
        "food_name" : "Манты",
        "food_price": 210,
        "food_time_to_deliver": "90 минут",
        "portion": "500 грамм"
    },
    {
        "food_name" : "Плов",
        "food_price": 190,
        "food_time_to_deliver": "150 минут",
        "portion": "600 грамм"
    },
    {
        "food_name" : "Лагман",
        "food_price": 170,
        "food_time_to_deliver": "120 минут",
        "portion": "600 грамм"
    },
    {
        "food_name" : "Манты",
        "food_price": 210,
        "food_time_to_deliver": "90 минут",
        "portion": "500 грамм"
    }
]


def home(request):
    meal_data = {
        "meal": meal,
        "title": "Home"
    }
    return render(
        request=request,
        template_name='home/home.htm',
        context=meal_data
        )