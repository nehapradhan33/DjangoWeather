from django.shortcuts import render

import requests

def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=91ab0f013c70ed1c221ab06ce0cbb420'
	city = 'london'

	r = requests.get(url.format(city)).json()
	

	city_weather = {
	'city': city,
	'temperature': r['main']['temp'],
	'description' : r['weather'][0]['description'],
	'icon' : r['weather'][0]['icon'],

	}
	print(city_weather)
	context = {'city_weather' : city_weather}
	return render(request, 'weather/weather.html', context)
