from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_app.models import Restaurant, Dish

def index(request):
    return render(request, "index.html")

def restaurants(request):
    restaurants = Restaurant.objects.all()
   
    return render(request, "restaurants.html", {"restaurants": restaurants, "new_var": 1})

def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return HttpResponse(f"<p>Restaurant details for restaurant with id = {restaurant_id}.</p><p> Restaurant name: {restaurant.name}, capacity: {restaurant.capacity}</p>")

def dishes(request):
    dishes = Dish.objects.all()

    return render(request, "dishes.html", {"dishes": dishes, "count": len(dishes)})

def dish_detail(request, dish_id):
    try:
        dish = Dish.objects.get(id=dish_id)
    except Dish.DoesNotExist:
        raise Http404("Dish does not exists!")

    return HttpResponse(dish)