from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .models import City

# Create your views here.


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=2bdf974667d0a14c259dfef722798e24'
    template = 'weather/weather.html'
    cities = City.objects.all().order_by('city')
    weather_cities = []
    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'id': city.id,
            'city': city.city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_cities.append(city_weather)

    context = {
        'city_weather': weather_cities
    }

    if request.method == 'POST':
        print(City.objects.filter(city=request.POST['city']).count())
        if City.objects.filter(city=request.POST['city']).count() >= 1:
            context['error_message'] = 'City already exists'
            return render(request, template, context)
        else:
            if requests.get(url.format(request.POST['city'])).json()['cod'] == 200:
                City.objects.create(city=request.POST['city'])
            else:
                context['error_message'] = 'Invalid City'
                return render(request, template, context)
            return redirect('weather:index')

    return render(request, template, context)


def delete(request, city_id):
    City.objects.get(id=city_id).delete()
    return redirect('weather:index')
