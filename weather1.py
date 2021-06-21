import requests
 
API_key = "1d7412aa1d86361fe2fa33b5b82d031c"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
city_name = input("Enter City Name : ")
 
Final_url = base_url + "appid=" + API_key + "&q=" + city_name
weather_data = requests.get(Final_url).json()

temp = weather_data['main']['temp']
 


wind_speed = weather_data['wind']['speed']
 

description = weather_data['weather'][0]['description']

latitude = weather_data['coord']['lat']
 

longitude = weather_data['coord']['lon']

print('\nTemperature : ',temp)
print('\nWind Speed : ',wind_speed)
print('\nDescription : ',description)
print('\nLatitude : ',latitude)
print('\nLongitude : ',longitude)
