from django.shortcuts import render
import requests
from .models import SearchCity

# Create your views here.
def main(request):
    # city = request.POST.get('city')

    return render(request, 'main.html')

def search(request):
    if request.method == 'POST':
        API_key = '6621546e1a94625a215c063e4320d66d'
        city = request.POST.get('city')
        API = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_key}'
        data = requests.get(API).json()
        max_temp=data ['main']['temp_max']
        min_temp=data['main']['temp_min']
        condition=data['weather'][0]['main']
        feels_like=data['main']['feels_like']
        icon=data['weather'][0]['icon']
        print(city)
        temp = data["main"]["temp"]
        
        
        

        city= request.POST.get('city')
        searchedCity= SearchCity()
        searchedCity.city=request.POST.get('city')
        searchedCity.temperature=temp
        searchedCity.save()


        all_context={'data':data, 'city':city.title(), 'temp':temp,'max_temp':max_temp,'mini_temp':min_temp,'condition':condition, 'feels_like':feels_like,'icon': icon}
        return render(request,'main.html',context=all_context)
def city(request):
    cities= SearchCity.objects.all()
    return render(request, 'city.html', {'cities': cities})

