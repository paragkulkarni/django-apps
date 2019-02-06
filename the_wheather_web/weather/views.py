from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests

# Create your views here.


def home_city(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=7b62ec83e6a5f746582fbf0b7db1469a'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    city_name = request.POST.get('city')

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city.name)).json()
        city_weather = {
            'city':city.name,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    #print(weather_data)

    context = {'weather_data':weather_data,'form':form}
    return render(request,'weather/home.html',context)
