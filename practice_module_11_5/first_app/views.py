from django.shortcuts import render

# Create your views here.
def app_home(request):
    meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "description": "A popular Canadian pastry shaped like a beaver's tail, typically topped with sugar, cinnamon, or various other sweet toppings."
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "description": "Crispy and savory potatoes seasoned and cooked to perfection, often served as a hearty breakfast side dish."
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "description": "A classic Canadian dessert with a flaky pastry shell filled with a sweet, buttery, and gooey filling."
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "description": "A famous deli meat from Montreal, typically served in a sandwich with mustard on rye bread."
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "description": "A no-bake dessert bar originating from Nanaimo, British Columbia, featuring layers of chocolate, custard, and coconut."
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
            "description": "A French-Canadian version of shepherd's pie, made with layers of ground beef, corn, and mashed potatoes."
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "description": "A traditional Quebecois dessert made with cake batter and hot caramel sauce, resulting in a moist, pudding-like cake."
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "description": "A quintessential Canadian dish consisting of fries topped with cheese curds and smothered in gravy."
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "description": "A traditional Acadian dish made from grated potatoes and meat, typically chicken or pork, baked to a golden brown."
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "description": "A hearty and comforting soup made from dried split peas, ham, and vegetables, often enjoyed during colder months."
        }
    ]
    return render(request, 'index.html', context = {'data' : meals})